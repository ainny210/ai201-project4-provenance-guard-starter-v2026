# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7 **before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The detector is accurate"* is an opinion — and perfect AI detection isn't possible anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1 false positive in 10 because on a writing site a wrong accusation costs more than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area            | A question it could answer                                    |
| --------------- | ------------------------------------------------------------- |
| False positives | How often may a human's writing get called AI?                |
| Score spread    | How far apart should clearly-AI and clearly-human text score? |
| Label coverage  | Is every one of your three labels actually reachable?         |
| The appeal path | Does an appeal always change status and always get recorded?  |
| Bad input       | What happens when `text` is missing, empty, or enormous?      |

Two things worth knowing before you pick numbers:

* **The expensive mistake is one-sided.** Missing some AI text costs the site a little. Accusing a real writer costs that person a lot. A criterion that treats both errors as equally bad is describing a system nobody would ship.
* **Unit 8 tests across three trials, and the target has to hold across all three.** Your first signal runs a model, so identical input can score differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is a **miss**.

---

## 1. False positives

Of 10 writing samples that I wrote myself without AI assistance, no more than 1 should receive the high-confidence AI label.

**Why this target:** A false accusation can damage a writer's reputation. I want the system to be cautious when identifying human writing as AI-generated.

---

## 2. Score spread

Across 10 clearly AI-generated samples and 10 human-written samples, the average AI-generated confidence score should be at least 0.20 higher than the average human-written confidence score.

**Why this target:** The two detection signals should distinguish between different writing patterns. A difference of 0.20 would provide evidence that the combined score is useful rather than arbitrary.

---

## 3. Label coverage

All three labels—human-leaning, uncertain, and AI-leaning—must appear at least once when testing 30 varied writing samples.

**Why this target:** A writing platform needs to communicate different confidence levels. If one label never appears, the thresholds may not be useful.

---

## 4. Appeal path

For 10 valid appeals against existing submissions, all 10 must change the submission status to `appealed` and create an appeal log entry.

**Why this target:** Writers must have a reliable way to challenge a classification. An appeal should never disappear without being recorded.

---

## 5. Bad input

For 10 invalid submissions containing missing text, empty text, incorrect data types, or excessively long text, all 10 must return an HTTP 4xx response rather than an HTTP 500 error.

**Why this target:** The service should reject invalid input safely without crashing or unnecessarily running the detection model.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

        ## 2. Uncertain cases land in the unsure band

        The system handles uncertain cases well.

        **Why this target:** ...

        > **Revised in unit 8:** Text I judged borderline scores between
        > 0.4 and 0.6 in at least 4 of 5 cases.
        >
        > **Why revised:** "well" gave me nothing to check. I couldn't
        > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

        ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
          of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

Unit 9: Capstone Acceptance Criteria
Project: Provenance Guard, an AI content detection system
Selected Shape: Shape A  Deploy and Instrument
Execution Path: Path B  Local with Logs
Extension Scope
I am adding request timing and JSON logs to my Flask app. This will help me monitor the app, find problems, and check its speed. I am not changing the AI detection logic.
I will test each of the five criteria below three times. Then I will make one improvement and test all five again.
Criterion 1: Structured Request Logging
Acceptance Criterion:
When I send 10 test requests (5 to /ping and 5 invalid requests to /submit), 10 out of 10 should create a valid JSON log entry. Each entry must include the timestamp, HTTP method, endpoint, status code, and how long the request took.
Why I Chose This Target:
Logs only help if every request is recorded. If some requests are missing, I can't trust the logs when I'm trying to find a problem. The app runs on my own computer and I control the tests, so I expect every request to be logged.

Criterion 2: Request Processing Time
Acceptance Criterion:
Over 10 requests in a row to /ping, the average server-side processing time should be under 50 milliseconds.
Why I Chose This Target:
/ping is a simple endpoint that does very little work. It should take only a few milliseconds on my computer. I chose 50 ms to allow some variation. If it goes over 50 ms, I will investigate whether my logging code is slowing the app down.

Criterion 3: Failed Request Visibility
Acceptance Criterion:
When I send 10 invalid requests to /submit (including missing text, empty text, incorrect data types, and oversized text), 10 out of 10 should return the expected HTTP 400 or 413 response and create a structured log entry showing the request was rejected.
Why I Chose This Target:
Bad requests can point to bugs or misuse. If they aren't logged, I can't see them. With a log entry for each one, I can check when it happened, which endpoint it hit, and why it failed.

Criterion 4: Local Service Reliability
Acceptance Criterion:
Over 10 requests in a row to the running app (5 to /ping and 5 invalid requests to /submit), all 10 should return their expected HTTP responses without unexpected HTTP 500 errors.
Why I Chose This Target:
Adding logging should not break the app. It worked before this change, so it should still work after. If my new code causes crashes, it is doing more harm than good.

Criterion 5: Log Completeness and Data Privacy
Acceptance Criterion:
Out of 10 request log entries generated from /submit requests, all 10 should include input metadata (text_length), HTTP status code, timestamp, and processing duration. None should contain the full submitted text.
Why I Chose This Target:
I need enough detail to fix problems. For example, knowing a submission was 3,000 characters and took 250 ms is useful. But users submit their own writing, and that shouldn't be stored in request log files. Logging the details without the actual text keeps users' work private.
Testing Commitment
I will test all five criteria three times before changing anything. Then I will find one weakness I can measure, fix it, and test all five criteria three more times.
I will not change my targets after seeing the results. I will mark each criterion MET or MISSED based on what I record.


