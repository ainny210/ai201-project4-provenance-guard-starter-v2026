# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 22:59
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `ed108c67-4585-49e1-a794-4826876684e7` | unsure | 0.376 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9b361c0d-79c0-4bdd-a5a0-85d91e36edbb` | unsure | 0.453 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c44b0158-beb1-409b-92a6-33c04fcaae4d` | unsure | 0.572 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `393a8d9a-44d5-4acc-9ef2-911ee2f9e834` | unsure | 0.596 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `fa703a94-b88a-49b4-b520-2bff9671f0a2` | unsure | 0.353 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `6c439983-8f3b-40c7-bbf5-664df97c5dd1` | unsure | 0.440 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `67e5e4f5-56a1-42bd-b263-d427eb851006` | unsure | 0.619 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `7d88146e-4a03-4915-bd0f-59bd71d61926` | unsure | 0.352 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `d677d6c0-3524-482e-8227-831734d20deb` | unsure | 0.587 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `10e8331e-ae24-4795-b158-fd8579a4c63f` | ai | 0.848 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3c2eea3f-83bf-41e2-a31e-f2f3d07533f1` | unsure | 0.569 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `d8b03f35-d39a-4dbd-bb79-1e1134c2569d` | ai | 0.676 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `51b2c428-f985-4fd9-909b-2a5353a8f786` | ai | 0.690 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `62dd5f7c-9b27-435d-9022-14ebd35bc2ea` | ai | 0.676 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `2a74d771-f806-49de-a712-4c73f5acddeb` | ai | 0.714 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `d2a4ef6b-4f62-4963-acf0-072d006b018f` | ai | 0.683 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d31fb087-1f3a-463e-afb8-0b4e570da498` | ai | 0.681 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `aa92ad89-bf2f-4e1c-8991-30dd897f724b` | human | 0.295 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `dea2af95-15a3-432e-a127-b10ca21d2753` | unsure | 0.416 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `98d044a0-d6e8-4573-b1fa-cb0ee8534415` | human | 0.274 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `78d1e732-d890-4e2f-b86b-1a9403bb65ae` | unsure | 0.553 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `e077eec1-af0d-4ce5-96df-9f93bed5c523` | unsure | 0.497 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `31b1dcc3-42a1-4440-8596-781c2522ca43` | unsure | 0.504 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `ece369bc-7d3d-41a0-b6fe-97b595e84af1` | unsure | 0.543 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `7296a3e2-7133-4e41-b443-f64290da5921` | human | 0.325 |  |
| MF04 | malformed | text is only punctuation | 200 | `0d4fea24-8469-4a91-999d-cbd8f5885050` | human | 0.256 |  |
| MF05 | malformed | text is a very long single word | 200 | `09cb376d-e1df-438a-acf4-9847807f951e` | ai | 0.824 |  |
| MF06 | malformed | text is emoji only | 200 | `fbf89b8c-fc21-4026-b916-e69a347510e6` | ai | 0.749 |  |
| MF07 | malformed | text is right-to-left script | 200 | `67d93a0b-065c-4be9-accf-b7764dea6a7e` | ai | 0.703 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `e66cdef3-a6c9-46cd-abfd-4a24e83601da` | unsure | 0.422 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `40f6680b-b2dd-427e-9995-9a40c31e2cff` | human | 0.317 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `10db630a-adec-4c15-a442-bdedc2105495` | human | 0.317 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9f6cc20b-aef1-4b50-9880-675dd163d5ca` | human | 0.317 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `72f4cda4-6b36-4b20-84e4-18e1c8850e16` | human | 0.317 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c9208ff7-502e-4b52-9c6e-422d6eded595` | human | 0.317 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `088b5833-e95a-4e25-99ea-a0c37aa9fe68` | human | 0.317 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2785849a-8ad8-4034-99ae-6cdd0c210f51` | human | 0.317 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ebce0937-b594-4f3e-9d0d-565094e60dea` | human | 0.317 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `707c8f29-0cdf-475b-9c9b-cd6dcbd902eb` | human | 0.317 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d850236a-23b4-40ae-be61-86224739e572` | human | 0.317 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "ed108c67-4585-49e1-a794-4826876684e7",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3763,
  "model_score": 0.1635,
  "style_score": 0.5891,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "9b361c0d-79c0-4bdd-a5a0-85d91e36edbb",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4531,
  "model_score": 0.5943,
  "style_score": 0.3118,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c44b0158-beb1-409b-92a6-33c04fcaae4d",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5717,
  "model_score": 0.6662,
  "style_score": 0.4772,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "393a8d9a-44d5-4acc-9ef2-911ee2f9e834",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5955,
  "model_score": 0.6114,
  "style_score": 0.5796,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "fa703a94-b88a-49b4-b520-2bff9671f0a2",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.353,
  "model_score": 0.3212,
  "style_score": 0.3849,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "6c439983-8f3b-40c7-bbf5-664df97c5dd1",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4395,
  "model_score": 0.5727,
  "style_score": 0.3063,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "67e5e4f5-56a1-42bd-b263-d427eb851006",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6194,
  "model_score": 0.5862,
  "style_score": 0.6526,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "7d88146e-4a03-4915-bd0f-59bd71d61926",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3525,
  "model_score": 0.2452,
  "style_score": 0.4599,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "d677d6c0-3524-482e-8227-831734d20deb",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5871,
  "model_score": 0.7042,
  "style_score": 0.47,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "10e8331e-ae24-4795-b158-fd8579a4c63f",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8478,
  "model_score": 0.9792,
  "style_score": 0.7165,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "3c2eea3f-83bf-41e2-a31e-f2f3d07533f1",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5693,
  "model_score": 0.6175,
  "style_score": 0.5211,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "d8b03f35-d39a-4dbd-bb79-1e1134c2569d",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.676,
  "model_score": 0.7387,
  "style_score": 0.6132,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "51b2c428-f985-4fd9-909b-2a5353a8f786",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6895,
  "model_score": 0.8051,
  "style_score": 0.5738,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "62dd5f7c-9b27-435d-9022-14ebd35bc2ea",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6762,
  "model_score": 0.8329,
  "style_score": 0.5194,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "2a74d771-f806-49de-a712-4c73f5acddeb",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7137,
  "model_score": 0.8005,
  "style_score": 0.627,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "d2a4ef6b-4f62-4963-acf0-072d006b018f",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6835,
  "model_score": 0.8814,
  "style_score": 0.4857,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "d31fb087-1f3a-463e-afb8-0b4e570da498",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.681,
  "model_score": 0.8816,
  "style_score": 0.4803,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "aa92ad89-bf2f-4e1c-8991-30dd897f724b",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2954,
  "model_score": 0.3223,
  "style_score": 0.2685,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "dea2af95-15a3-432e-a127-b10ca21d2753",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4158,
  "model_score": 0.4625,
  "style_score": 0.3692,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "98d044a0-d6e8-4573-b1fa-cb0ee8534415",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2736,
  "model_score": 0.2044,
  "style_score": 0.3427,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "78d1e732-d890-4e2f-b86b-1a9403bb65ae",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5529,
  "model_score": 0.5943,
  "style_score": 0.5114,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "e077eec1-af0d-4ce5-96df-9f93bed5c523",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4969,
  "model_score": 0.4998,
  "style_score": 0.4939,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "31b1dcc3-42a1-4440-8596-781c2522ca43",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5038,
  "model_score": 0.6401,
  "style_score": 0.3675,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "ece369bc-7d3d-41a0-b6fe-97b595e84af1",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.543,
  "model_score": 0.5583,
  "style_score": 0.5277,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the s",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "7296a3e2-7133-4e41-b443-f64290da5921",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.325,
  "model_score": 0.0,
  "style_score": 0.65,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "0d4fea24-8469-4a91-999d-cbd8f5885050",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2556,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "09cb376d-e1df-438a-acf4-9847807f951e",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8238,
  "model_score": 0.9976,
  "style_score": 0.65,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "fbf89b8c-fc21-4026-b916-e69a347510e6",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7485,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "67d93a0b-065c-4be9-accf-b7764dea6a7e",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "e66cdef3-a6c9-46cd-abfd-4a24e83601da",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.422,
  "model_score": 0.2395,
  "style_score": 0.6045,
  "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "40f6680b-b2dd-427e-9995-9a40c31e2cff",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "10db630a-adec-4c15-a442-bdedc2105495",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "9f6cc20b-aef1-4b50-9880-675dd163d5ca",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "72f4cda4-6b36-4b20-84e4-18e1c8850e16",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c9208ff7-502e-4b52-9c6e-422d6eded595",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "088b5833-e95a-4e25-99ea-a0c37aa9fe68",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "2785849a-8ad8-4034-99ae-6cdd0c210f51",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "ebce0937-b594-4f3e-9d0d-565094e60dea",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "707c8f29-0cdf-475b-9c9b-cd6dcbd902eb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "d850236a-23b4-40ae-be61-86224739e572",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3166,
  "model_score": 0.0287,
  "style_score": 0.6045,
  "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
