# Attack run — after_fix

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 12:53
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `032d188c-4a34-475b-acc9-8314efe9e26c` | unsure | 0.376 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9d18854b-0436-4abf-a306-b3ae46bfd244` | unsure | 0.453 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `1d6b73e5-e32f-430b-a673-2a3052e2828a` | unsure | 0.572 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `45ed207e-4720-436f-877e-bba17d7b89c7` | unsure | 0.596 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `44c49888-6f85-46e2-9955-83c052a379d8` | unsure | 0.353 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `37b176cd-9306-4bd4-8054-7b9ee76d86d1` | unsure | 0.440 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `b0b2be08-f70d-4d1a-9d76-d24fd05f0934` | unsure | 0.619 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `afb80c91-62d3-4b8e-be5a-f19a8ab59efa` | unsure | 0.352 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `41bde1ba-2dea-4e1c-b615-e8b10690cfd1` | unsure | 0.587 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `8558e7c1-7728-483e-9da8-2d15c878c223` | ai | 0.848 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `d9bc33e9-a0bd-4919-bb11-0731649cc8bd` | unsure | 0.569 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `6fc14105-8329-459f-b590-bcd103e5c4c2` | ai | 0.676 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `8cd74a05-ca68-4780-a9a9-95d97508d2ae` | ai | 0.690 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c7a71356-fb6b-4b8a-a99f-c36461d07fd0` | ai | 0.676 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `3539dff2-f33b-496c-952e-d70ec5643509` | ai | 0.714 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `22eec625-f766-45b2-83cb-e43dfaede442` | ai | 0.683 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f9120c69-b731-4998-b13d-6b5ccb9842e0` | ai | 0.681 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `a8ee6e1c-c001-440f-952b-99985d3c68fe` | human | 0.295 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `5dfb90d5-fcc9-46ca-b72e-efaeff6d0f75` | unsure | 0.416 | REVIEW |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `0e712b42-1ce3-4af8-ad58-a676c8b6eced` | human | 0.274 | REVIEW |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `a8ec6800-cd8a-4967-bd3a-7ef65084be9c` | unsure | 0.553 | REVIEW |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `a42ad52d-1b36-40b0-9763-8ccbb6782f45` | unsure | 0.497 | REVIEW |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a5885586-5d5b-44cd-b053-989024d89c66` | unsure | 0.504 | REVIEW |
| PI06 | prompt_injection | instruction plus real human text | 200 | `417e1103-dcae-48c6-9b21-1f10d6b8eff3` | unsure | 0.543 | REVIEW |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `1e7177fc-9167-46c2-a683-e01a40503aaf` | human | 0.325 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `890cd559-dd46-4732-9566-eef868dcf3d2` | human | 0.256 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `1cecc1b7-8dfb-4504-81e6-8f583ac5a221` | ai | 0.824 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `3caf3108-aaa7-41f4-a350-49e084d3f11e` | ai | 0.749 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `ccd350be-fc7c-4dc2-8d83-2ac5d84eb0fa` | ai | 0.703 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `ae86103a-dcb3-4f0a-b81f-9daec32f55a0` | unsure | 0.422 | BROKE |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `27490285-e34d-48a6-ac09-d707616769b6` | human | 0.317 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c0aa3802-c21d-4fad-a459-7854f6502210` | human | 0.317 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `898667fe-895e-4c62-a2cf-07896ad1d948` | human | 0.317 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `457909e7-df29-4b78-bb16-57c85e236076` | human | 0.317 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fcd745fe-561b-4418-a85c-53033f0a3ff6` | human | 0.317 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `53dcb842-9719-49d7-a06a-aba6d5b92773` | human | 0.317 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9547feca-f9b6-45d4-ba6e-53b805bb7a49` | human | 0.317 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5d7b84c0-849e-42ba-8115-d01550c3414a` | human | 0.317 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2c6217eb-7387-4985-bf9d-06ff97f7f447` | human | 0.317 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3f181880-033a-425c-bf75-cba0e8213c3c` | human | 0.317 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
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
  "content_id": "032d188c-4a34-475b-acc9-8314efe9e26c",
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
  "content_id": "9d18854b-0436-4abf-a306-b3ae46bfd244",
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
  "content_id": "1d6b73e5-e32f-430b-a673-2a3052e2828a",
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
  "content_id": "45ed207e-4720-436f-877e-bba17d7b89c7",
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
  "content_id": "44c49888-6f85-46e2-9955-83c052a379d8",
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
  "content_id": "37b176cd-9306-4bd4-8054-7b9ee76d86d1",
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
  "content_id": "b0b2be08-f70d-4d1a-9d76-d24fd05f0934",
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
  "content_id": "afb80c91-62d3-4b8e-be5a-f19a8ab59efa",
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
  "content_id": "41bde1ba-2dea-4e1c-b615-e8b10690cfd1",
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
  "content_id": "8558e7c1-7728-483e-9da8-2d15c878c223",
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
  "content_id": "d9bc33e9-a0bd-4919-bb11-0731649cc8bd",
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
  "content_id": "6fc14105-8329-459f-b590-bcd103e5c4c2",
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
  "content_id": "8cd74a05-ca68-4780-a9a9-95d97508d2ae",
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
  "content_id": "c7a71356-fb6b-4b8a-a99f-c36461d07fd0",
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
  "content_id": "3539dff2-f33b-496c-952e-d70ec5643509",
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
  "content_id": "22eec625-f766-45b2-83cb-e43dfaede442",
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
  "content_id": "f9120c69-b731-4998-b13d-6b5ccb9842e0",
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
  "content_id": "a8ee6e1c-c001-440f-952b-99985d3c68fe",
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
  "content_id": "5dfb90d5-fcc9-46ca-b72e-efaeff6d0f75",
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
  "content_id": "0e712b42-1ce3-4af8-ad58-a676c8b6eced",
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
  "content_id": "a8ec6800-cd8a-4967-bd3a-7ef65084be9c",
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
  "content_id": "a42ad52d-1b36-40b0-9763-8ccbb6782f45",
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
  "content_id": "a5885586-5d5b-44cd-b053-989024d89c66",
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
  "content_id": "417e1103-dcae-48c6-9b21-1f10d6b8eff3",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "1e7177fc-9167-46c2-a683-e01a40503aaf",
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
  "content_id": "890cd559-dd46-4732-9566-eef868dcf3d2",
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
  "content_id": "1cecc1b7-8dfb-4504-81e6-8f583ac5a221",
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
  "content_id": "3caf3108-aaa7-41f4-a350-49e084d3f11e",
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
  "content_id": "ccd350be-fc7c-4dc2-8d83-2ac5d84eb0fa",
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
  "content_id": "ae86103a-dcb3-4f0a-b81f-9daec32f55a0",
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
  "content_id": "27490285-e34d-48a6-ac09-d707616769b6",
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
  "content_id": "c0aa3802-c21d-4fad-a459-7854f6502210",
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
  "content_id": "898667fe-895e-4c62-a2cf-07896ad1d948",
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
  "content_id": "457909e7-df29-4b78-bb16-57c85e236076",
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
  "content_id": "fcd745fe-561b-4418-a85c-53033f0a3ff6",
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
  "content_id": "53dcb842-9719-49d7-a06a-aba6d5b92773",
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
  "content_id": "9547feca-f9b6-45d4-ba6e-53b805bb7a49",
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
  "content_id": "5d7b84c0-849e-42ba-8115-d01550c3414a",
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
  "content_id": "2c6217eb-7387-4985-bf9d-06ff97f7f447",
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
  "content_id": "3f181880-033a-425c-bf75-cba0e8213c3c",
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

