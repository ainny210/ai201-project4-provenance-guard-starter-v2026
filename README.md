# Provenance Guard

> ### ðŸ‘‹ Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> In another terminal:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
>
> Everything this unit is filling in the middle.

---

# UNIT 7 â€” THE BUILD

## What This Does

Provenance Guard is a Flask web application that analyzes submitted writing and estimates whether it contains patterns associated with AI-generated text.

The application does not prove whether a person used AI. It provides a classification based on two automated signals.

When someone submits writing, the application follows these steps:

1. The user sends a text submission and creator ID to `POST /submit`.
2. The Flask application validates the request and checks that the text is not empty or too long.
3. `detector.py` calculates a GPT-2 model score.
4. `stylometry.py` calculates a writing-style score based on sentence variation, vocabulary diversity, and punctuation.
5. `scoring.py` combines both scores into one confidence value.
6. The confidence is mapped to one of three classifications: `human`, `unsure`, or `ai`.
7. The application returns the result and records the decision in `logs/audit.jsonl`.

The response includes a unique `content_id`, the classification, the confidence score, an explanation, and both individual signal scores.

If a writer disagrees with the result, they can submit an appeal through `POST /appeal`.

The appeal is recorded in the audit log with the status `under_review` so that the result can be reviewed by a person.

---

## Signals and Scoring

### Signal one â€” the model signal

**What it measures:**

The first signal uses a GPT-2 language model to evaluate how predictable the submitted text is according to the model.

The result is converted into a score between 0 and 1, where a higher value indicates more AI-like writing patterns.

This signal is implemented in `detector.py`, in the `model_signal()` function.

**Why that might differ between human and AI writing:**

AI-generated writing may follow predictable language patterns because language models generate text based on likely word sequences.

Human writing can sometimes have more unexpected wording, although this is not always true.

**What it can't see:**

The model cannot identify the actual author.

A human writer can produce very predictable writing, especially when writing formally or using common phrases.

AI-generated text can also be edited to become less predictable.

Because of these limitations, the model score should not be treated as proof of AI use.

### Signal two â€” the style signal

**What it measures:**

The second signal measures writing characteristics without trying to understand the meaning of the text.

It uses three measurements:

1. **Sentence-length spread:** Measures how much sentence lengths vary. It uses the standard deviation of sentence lengths divided by their mean.
2. **Type-token ratio:** Measures vocabulary diversity by dividing the number of unique words by the total number of words.
3. **Punctuation density:** Measures the number of punctuation marks relative to the number of characters.

These functions are implemented in `stylometry.py`.

**Why that might differ between human and AI writing:**

Some AI-generated writing has relatively consistent sentence lengths and repetitive vocabulary.

Human writing may have more variation in sentence structure, word choice, and punctuation.

I convert each measurement into a score where a higher value represents more AI-like patterns.

The style signal uses the following weights:

* Sentence-length variation: 40%
* Vocabulary diversity: 35%
* Punctuation density: 25%

The measurements are normalized before they are combined.

**What it can't see:**

Stylometry cannot understand what the writing means or identify its author.

A short text may not contain enough sentences for meaningful variation.

A person can also change the score by adding punctuation, changing sentence lengths, or replacing words.

This means stylometry can be affected by simple editing, even when the actual authorship does not change.

### The combining rule

**The rule:**

I use a weighted average of the model signal and the style signal.

Both signals receive equal importance.

If the signals disagree, neither signal automatically determines the final classification. Instead, the combined confidence falls between their individual scores.

**The numbers:**

```text
confidence = (0.50 Ã— model_score) + (0.50 Ã— style_score)
```

The confidence score is limited to the range 0â€“1.

**Where it lives:** `scoring.py::combine_signals`

The weights and classification thresholds are defined in `config.py`.

**A case where my two signals split, and what my rule does with it:**

I tested the following submission:

> Artificial intelligence is changing the way people work. It helps people analyze information, generate ideas, and complete tasks more efficiently.

The actual results were:

```text
model_score = 0.7748
style_score = 0.4859
confidence = 0.6303
guess = unsure
```

The model signal was relatively high, but the style signal was lower.

The weighted average was:

```text
(0.7748 Ã— 0.50) + (0.4859 Ã— 0.50) = 0.63035
```

The application returned a confidence of approximately 0.6303.

Because this score was below the AI classification threshold of 0.65, the result was `unsure`.

This example shows why I did not rely on only one signal.

---

## Label Variants

The application uses three labels.

| Label | Score

<!-- UNIT8_FINAL_START -->

# Unit 8 ? Provenance Guard Testing and Improvement

## Project Overview

This project evaluates a text provenance classifier that combines a GPT-2 perplexity-based model signal with a stylometric signal. The service exposes submission, appeal, health, and audit-log endpoints.

The testing focused on false positives, AI-versus-human confidence separation, classification coverage, appeals, malformed requests, rate limiting, and adversarial attacks.

## Rate Limiting

Rate limiting was implemented using Flask-Limiter.

Configured limits:
- 10 submissions per minute per creator
- 200 submissions per day per creator

During the staff attack run, the flood sequence produced 10 successful HTTP 200 responses followed by 2 HTTP 429 responses.

Rate-limit rejections were recorded in the audit log.

## Evaluation Scenarios

Five evaluation categories were prepared:

1. False positives on human-like writing
2. AI-versus-human confidence separation
3. Coverage of human, unsure, and AI classifications
4. Appeal workflow
5. Malformed submission handling

The BEFORE evaluation runner completed three trials and generated a saved report.

Important limitation: the human-like diagnostic samples were AI-generated placeholders, not independently verified human-authored samples. Therefore, the false-positive criterion and human-versus-AI confidence separation criterion cannot be claimed as validated.

The appeal workflow was not fully evaluated through the runner.

## BEFORE Attack Run

The provided staff attack set contained 56 attacks.

The BEFORE attack run completed and generated a report covering evasion, false-positive, malformed-request, and other adversarial cases.

The results exposed several concerning false-positive classifications and a malformed-input server error.

## Identified Vulnerability ? MF02

Attack MF02 submitted a single-character input:

    a

Before the improvement, the application returned HTTP 500.

This indicated insufficient validation before passing the input to the detector.

## Implemented Improvement

Input validation was added to the submission endpoint.

The updated service rejects text shorter than two non-whitespace characters before running the detector.

Invalid submissions are recorded through the audit rejection mechanism.

The improvement preserves the existing GPT-2 and stylometry scoring approach.

## Measured Before-and-After Result

| Attack | Before | After | Result |
|---|---|---|---|
| MF02 | HTTP 500 | HTTP 400 | Improved malformed-input handling |

The targeted AFTER test verified that MF02 returned HTTP 400.

This is the confirmed measured improvement.

## AFTER Attack Testing

Additional AFTER attack runs were attempted.

EV01 did not receive an HTTP response and was marked BROKE by the attack harness.

The detailed error was:

    ReadTimeout: HTTPConnectionPool(host='127.0.0.1', port=5000):
    Read timed out. (read timeout=180.0)

Flask health checks continued returning HTTP 200, but the GPT-2 model was not loaded.

Independent testing showed Python becoming unresponsive during the PyTorch import.

A subsequent attempt to repair the PyTorch installation was unsuccessful within the available time.

Consequently, the full AFTER attack suite and AFTER evaluation were not completed successfully.

## Audit Evidence

The application generated an audit trail of classification decisions and rejected submissions.

An audit export was saved to:

    results/audit_extract.json

The audit log includes rate-limit rejection events.

## Remaining Limitations

- The classifier can incorrectly label human writing as AI.
- The evaluation does not establish reliable AI-versus-human score separation.
- Ten successful appeals with the required status were not verified.
- The complete malformed-input criterion was not verified after the improvement.
- The full AFTER attack run remains incomplete.
- PyTorch model loading became unresponsive during final testing.
- The minimum-length validation rejects legitimate single-character text as well as malformed detector inputs.
- Manual HELD/BROKE judgments for all staff attacks were not completed.

## Evidence Files

- results/run_2026-11-08_2252_before.md
- results/attack_run_2026-11-08_2259_before.md
- results/attack_run_2026-11-08_2305_after.md
- results/attack_run_2026-11-08_2314_after.md
- results/attack_run_2026-11-08_2337_after.md
- results/attack_run_2026-11-08_2344_after.md
- results/audit_extract.json

## How I Used AI

I used AI assistance to develop evaluation scenarios, implement and review input validation, troubleshoot Windows PowerShell and dependency problems, and organize the testing evidence.

I verified the MF02 improvement through the actual attack runner.

I did not treat AI-generated diagnostic samples as genuine human-authored writing or claim that incomplete tests passed.

## Conclusion

The project demonstrates rate limiting, audit logging, adversarial evaluation, and one verified security improvement.

The confirmed improvement is that MF02 changed from an HTTP 500 server error to an HTTP 400 client error.

Additional testing is required to establish that all five evaluation criteria pass.

<!-- UNIT8_FINAL_END -->
## Unit 8 — Actual Audit Log Evidence

The following ten entries are copied from the application's audit log.
Nine are completed submissions and one is a rejected request.

~~~json
{"timestamp":"2026-11-09T04:59:47+00:00","content_id":"10db630a-adec-4c15-a442-bdedc2105495","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6045,"combined_score":0.3166,"label":"Our automated analysis suggests this writing may be human-written. This result is not a guarantee.","status":"decided"}
{"timestamp":"2026-11-09T04:59:47+00:00","content_id":"9f6cc20b-aef1-4b50-9880-675dd163d5ca","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6045,"combined_score":0.3166,"label":"Our automated analysis suggests this writing may be human-written. This result is not a guarantee.","status":"decided"}
{"timestamp":"2026-11-09T04:59:47+00:00","content_id":"72f4cda4-6b36-4b20-84e4-18e1c8850e16","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6045,"combined_score":0.3166,"label":"Our automated analysis suggests this writing may be human-written. This result is not a guarantee.","status":"decided"}
{"timestamp":"2026-11-09T04:59:47+00:00","content_id":"c9208ff7-502e-4b52-9c6e-422d6eded595","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6045,"combined_score":0.3166,"label":"Our automated analysis suggests this writing may be human-written. This result is not a guarantee.","status":"decided"}
{"timestamp":"2026-11-09T04:59:47+00:00","content_id":"088b5833-e95a-4e25-99ea-a0c37aa9fe68","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6045,"combined_score":0.3166,"label":"Our automated analysis suggests this writing may be human-written. This result is not a guarantee.","status":"decided"}
{"timestamp":"2026-11-09T04:59:47+00:00","content_id":"2785849a-8ad8-4034-99ae-6cdd0c210f51","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6045,"combined_score":0.3166,"label":"Our automated analysis suggests this writing may be human-written. This result is not a guarantee.","status":"decided"}
{"timestamp":"2026-11-09T04:59:47+00:00","content_id":"ebce0937-b594-4f3e-9d0d-565094e60dea","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6045,"combined_score":0.3166,"label":"Our automated analysis suggests this writing may be human-written. This result is not a guarantee.","status":"decided"}
{"timestamp":"2026-11-09T04:59:47+00:00","content_id":"707c8f29-0cdf-475b-9c9b-cd6dcbd902eb","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6045,"combined_score":0.3166,"label":"Our automated analysis suggests this writing may be human-written. This result is not a guarantee.","status":"decided"}
{"timestamp":"2026-11-09T04:59:47+00:00","content_id":"d850236a-23b4-40ae-be61-86224739e572","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6045,"combined_score":0.3166,"label":"Our automated analysis suggests this writing may be human-written. This result is not a guarantee.","status":"decided"}
{"timestamp":"2026-11-09T05:05:11+00:00","creator_id":"attacker_MF02","event":"rejected","status":"rejected","reason":"text_too_short"}
~~~


## Unit 8 — Verified Rate-Limiting Test

### Configuration and rationale

- Per-minute limit: 10 submissions per creator.
- Daily limit: 200 submissions per creator.
- Storage: In-memory for local testing.

The 10-per-minute limit permits normal interactive use while restricting
rapid automated submission floods. The 200-per-day limit allows repeated
testing and legitimate revisions while limiting sustained abuse.

These thresholds are testing choices, not production-calibrated limits.
In-memory storage is suitable for this local demonstration but resets
when the application restarts and is not shared across server instances.

### Actual test results

Fifteen consecutive submissions were sent using the same creator ID.

| Request numbers | HTTP response | Result |
|---|---|---|
| 1–10 | 200 | Accepted |
| 11–15 | 429 | Rate limited |

Actual HTTP status sequence:

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

**Verdict: HELD.** The limiter rejected submissions after the tenth request within the test window.


## Unit 8 Final Verification — November 10, 2026

### Acceptance Criteria

| Criterion | Result | Evidence |
|---|---|---|
| Human false positives | PASS | 0/10 high-confidence AI classifications in each of 3 trials |
| AI vs human separation | PASS | Mean confidence difference: 0.2326 (target >= 0.20), across 3 trials |
| Classification coverage | PASS | human, unsure, and ai produced in all 3 trials |
| Appeal workflow | PASS | 10/10 appeals accepted; 10/10 matching audit records verified |
| Invalid requests | PASS | 30/30 returned HTTP 4xx across 3 trials |

### Measured Improvement

- Before detector weight adjustment: AI-human confidence difference = 0.1474.
- After adjustment (70% model, 30% stylometry): difference = 0.2326.
- Absolute improvement: +0.0852.
- Full attack suite: 56/56 executed.
- Server errors in final attack run: 0.
- MF02 malformed request: HTTP 400.
- Flood protection: first 10 requests HTTP 200, next 2 HTTP 429.
- Attack-specific security verdicts require manual review.

### Evidence Files

- results/run_2026-11-10_1337_updated_human_samples.md
- results/run_2026-11-10_1354_after_70_30.md
- results/appeal_verification.md
- results/appeal_audit_verification.csv
- results/attack_run_2026-11-10_1253_after_fix.md
- results/attack_run_2026-11-10_1409_after_70_30.md
- results/flood_2026-11-10_124430_verified.md

