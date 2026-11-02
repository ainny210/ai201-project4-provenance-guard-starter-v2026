# Provenance Guard

> ### 👋 Start here
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

# UNIT 7 — THE BUILD

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

### Signal one — the model signal

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

### Signal two — the style signal

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
confidence = (0.50 × model_score) + (0.50 × style_score)
```

The confidence score is limited to the range 0–1.

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
(0.7748 × 0.50) + (0.4859 × 0.50) = 0.63035
```

The application returned a confidence of approximately 0.6303.

Because this score was below the AI classification threshold of 0.65, the result was `unsure`.

This example shows why I did not rely on only one signal.

---

## Label Variants

The application uses three labels.

| Label | Score
