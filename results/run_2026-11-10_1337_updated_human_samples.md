# Run log — updated_human_samples

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-10 13:37

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. false positive diagnostic placeholders |  |   |   |   |  |
| 2. AI confidence score spread |  |   |   |   |  |
| 2. human confidence score spread placeholders |  |   |   |   |  |
| 3. label coverage |  |   |   |   |  |
| 5. bad input handling |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### false positive diagnostic placeholders

**Trial 1**

```json
[
  {
    "status": null,
    "error": "ConnectionError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))",
    "sent": "Yesterday i was working on my thesis project of my masters so i spent "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4129,
    "model_score": 0.1149,
    "style_score": 0.7109,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I had problem understanding one of the codepath assignments at first a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3703,
    "model_score": 0.0923,
    "style_score": 0.6483,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "My Laptop was running slowly when I opened a multiple excel file simul"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.1759,
    "style_score": 0.6684,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my new job i attend a meetings where we discussed how organizations"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5873,
    "model_score": 0.4649,
    "style_score": 0.7097,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was testing a Python application and noticed that some requests were"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4034,
    "model_score": 0.1706,
    "style_score": 0.6362,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Last week I reviewed many database security vulnerablities and some vu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3835,
    "model_score": 0.1181,
    "style_score": 0.6488,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my opinion testing is an important part of as SDLC part because app"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4145,
    "model_score": 0.1796,
    "style_score": 0.6494,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "During my Masters thesis research i created charts/graphs to compare v"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3669,
    "model_score": 0.0565,
    "style_score": 0.6773,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was learning about AI security in terms of policies GRC part and how"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3359,
    "model_score": 0.0133,
    "style_score": 0.6586,
    "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
    "sent": "From Last two days even today i working on flask application as i enab"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.424,
    "model_score": 0.1598,
    "style_score": 0.6882,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Yesterday i was working on my thesis project of my masters so i spent "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4129,
    "model_score": 0.1149,
    "style_score": 0.7109,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I had problem understanding one of the codepath assignments at first a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3703,
    "model_score": 0.0923,
    "style_score": 0.6483,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "My Laptop was running slowly when I opened a multiple excel file simul"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.1759,
    "style_score": 0.6684,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my new job i attend a meetings where we discussed how organizations"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5873,
    "model_score": 0.4649,
    "style_score": 0.7097,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was testing a Python application and noticed that some requests were"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4034,
    "model_score": 0.1706,
    "style_score": 0.6362,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Last week I reviewed many database security vulnerablities and some vu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3835,
    "model_score": 0.1181,
    "style_score": 0.6488,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my opinion testing is an important part of as SDLC part because app"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4145,
    "model_score": 0.1796,
    "style_score": 0.6494,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "During my Masters thesis research i created charts/graphs to compare v"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3669,
    "model_score": 0.0565,
    "style_score": 0.6773,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was learning about AI security in terms of policies GRC part and how"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3359,
    "model_score": 0.0133,
    "style_score": 0.6586,
    "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
    "sent": "From Last two days even today i working on flask application as i enab"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.424,
    "model_score": 0.1598,
    "style_score": 0.6882,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Yesterday i was working on my thesis project of my masters so i spent "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4129,
    "model_score": 0.1149,
    "style_score": 0.7109,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I had problem understanding one of the codepath assignments at first a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3703,
    "model_score": 0.0923,
    "style_score": 0.6483,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "My Laptop was running slowly when I opened a multiple excel file simul"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.1759,
    "style_score": 0.6684,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my new job i attend a meetings where we discussed how organizations"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5873,
    "model_score": 0.4649,
    "style_score": 0.7097,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was testing a Python application and noticed that some requests were"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4034,
    "model_score": 0.1706,
    "style_score": 0.6362,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Last week I reviewed many database security vulnerablities and some vu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3835,
    "model_score": 0.1181,
    "style_score": 0.6488,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my opinion testing is an important part of as SDLC part because app"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4145,
    "model_score": 0.1796,
    "style_score": 0.6494,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "During my Masters thesis research i created charts/graphs to compare v"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3669,
    "model_score": 0.0565,
    "style_score": 0.6773,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was learning about AI security in terms of policies GRC part and how"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3359,
    "model_score": 0.0133,
    "style_score": 0.6586,
    "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
    "sent": "From Last two days even today i working on flask application as i enab"
  }
]
```

### AI confidence score spread

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5901,
    "model_score": 0.5657,
    "style_score": 0.6146,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Artificial intelligence has fundamentally transformed modern computing"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.558,
    "model_score": 0.6129,
    "style_score": 0.5032,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Cybersecurity represents a critical component of modern digital infras"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6062,
    "model_score": 0.5995,
    "style_score": 0.613,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Machine learning algorithms identify patterns within structured and un"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5623,
    "model_score": 0.528,
    "style_score": 0.5965,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Database management systems provide essential mechanisms for storing, "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6691,
    "model_score": 0.7127,
    "style_score": 0.6255,
    "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
    "sent": "Effective risk management requires a systematic approach to identifyin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5832,
    "model_score": 0.5294,
    "style_score": 0.637,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The integration of artificial intelligence into enterprise environment"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3971,
    "model_score": 0.1863,
    "style_score": 0.6079,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Organizations should establish robust monitoring procedures, implement"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5886,
    "model_score": 0.5355,
    "style_score": 0.6417,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Natural language processing enables computational systems to interpret"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5393,
    "model_score": 0.4709,
    "style_score": 0.6076,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Software quality assurance involves systematic testing methodologies d"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5012,
    "model_score": 0.4099,
    "style_score": 0.5925,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Responsible artificial intelligence development requires transparency,"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5901,
    "model_score": 0.5657,
    "style_score": 0.6146,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Artificial intelligence has fundamentally transformed modern computing"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.558,
    "model_score": 0.6129,
    "style_score": 0.5032,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Cybersecurity represents a critical component of modern digital infras"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6062,
    "model_score": 0.5995,
    "style_score": 0.613,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Machine learning algorithms identify patterns within structured and un"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5623,
    "model_score": 0.528,
    "style_score": 0.5965,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Database management systems provide essential mechanisms for storing, "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6691,
    "model_score": 0.7127,
    "style_score": 0.6255,
    "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
    "sent": "Effective risk management requires a systematic approach to identifyin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5832,
    "model_score": 0.5294,
    "style_score": 0.637,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The integration of artificial intelligence into enterprise environment"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3971,
    "model_score": 0.1863,
    "style_score": 0.6079,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Organizations should establish robust monitoring procedures, implement"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5886,
    "model_score": 0.5355,
    "style_score": 0.6417,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Natural language processing enables computational systems to interpret"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5393,
    "model_score": 0.4709,
    "style_score": 0.6076,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Software quality assurance involves systematic testing methodologies d"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5012,
    "model_score": 0.4099,
    "style_score": 0.5925,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Responsible artificial intelligence development requires transparency,"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5901,
    "model_score": 0.5657,
    "style_score": 0.6146,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Artificial intelligence has fundamentally transformed modern computing"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.558,
    "model_score": 0.6129,
    "style_score": 0.5032,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Cybersecurity represents a critical component of modern digital infras"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6062,
    "model_score": 0.5995,
    "style_score": 0.613,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Machine learning algorithms identify patterns within structured and un"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5623,
    "model_score": 0.528,
    "style_score": 0.5965,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Database management systems provide essential mechanisms for storing, "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6691,
    "model_score": 0.7127,
    "style_score": 0.6255,
    "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
    "sent": "Effective risk management requires a systematic approach to identifyin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5832,
    "model_score": 0.5294,
    "style_score": 0.637,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The integration of artificial intelligence into enterprise environment"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3971,
    "model_score": 0.1863,
    "style_score": 0.6079,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Organizations should establish robust monitoring procedures, implement"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5886,
    "model_score": 0.5355,
    "style_score": 0.6417,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Natural language processing enables computational systems to interpret"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5393,
    "model_score": 0.4709,
    "style_score": 0.6076,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Software quality assurance involves systematic testing methodologies d"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5012,
    "model_score": 0.4099,
    "style_score": 0.5925,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Responsible artificial intelligence development requires transparency,"
  }
]
```

### human confidence score spread placeholders

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.424,
    "model_score": 0.1598,
    "style_score": 0.6882,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Yesterday i was working on my thesis project of my masters so i spent "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4129,
    "model_score": 0.1149,
    "style_score": 0.7109,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I had problem understanding one of the codepath assignments at first a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3703,
    "model_score": 0.0923,
    "style_score": 0.6483,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "My Laptop was running slowly when I opened a multiple excel file simul"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.1759,
    "style_score": 0.6684,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my new job i attend a meetings where we discussed how organizations"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5873,
    "model_score": 0.4649,
    "style_score": 0.7097,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was testing a Python application and noticed that some requests were"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4034,
    "model_score": 0.1706,
    "style_score": 0.6362,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Last week I reviewed many database security vulnerablities and some vu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3835,
    "model_score": 0.1181,
    "style_score": 0.6488,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my opinion testing is an important part of as SDLC part because app"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4145,
    "model_score": 0.1796,
    "style_score": 0.6494,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "During my Masters thesis research i created charts/graphs to compare v"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3669,
    "model_score": 0.0565,
    "style_score": 0.6773,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was learning about AI security in terms of policies GRC part and how"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3359,
    "model_score": 0.0133,
    "style_score": 0.6586,
    "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
    "sent": "From Last two days even today i working on flask application as i enab"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.424,
    "model_score": 0.1598,
    "style_score": 0.6882,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Yesterday i was working on my thesis project of my masters so i spent "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4129,
    "model_score": 0.1149,
    "style_score": 0.7109,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I had problem understanding one of the codepath assignments at first a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3703,
    "model_score": 0.0923,
    "style_score": 0.6483,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "My Laptop was running slowly when I opened a multiple excel file simul"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.1759,
    "style_score": 0.6684,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my new job i attend a meetings where we discussed how organizations"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5873,
    "model_score": 0.4649,
    "style_score": 0.7097,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was testing a Python application and noticed that some requests were"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4034,
    "model_score": 0.1706,
    "style_score": 0.6362,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Last week I reviewed many database security vulnerablities and some vu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3835,
    "model_score": 0.1181,
    "style_score": 0.6488,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my opinion testing is an important part of as SDLC part because app"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4145,
    "model_score": 0.1796,
    "style_score": 0.6494,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "During my Masters thesis research i created charts/graphs to compare v"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3669,
    "model_score": 0.0565,
    "style_score": 0.6773,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was learning about AI security in terms of policies GRC part and how"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3359,
    "model_score": 0.0133,
    "style_score": 0.6586,
    "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
    "sent": "From Last two days even today i working on flask application as i enab"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.424,
    "model_score": 0.1598,
    "style_score": 0.6882,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Yesterday i was working on my thesis project of my masters so i spent "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4129,
    "model_score": 0.1149,
    "style_score": 0.7109,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I had problem understanding one of the codepath assignments at first a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3703,
    "model_score": 0.0923,
    "style_score": 0.6483,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "My Laptop was running slowly when I opened a multiple excel file simul"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.1759,
    "style_score": 0.6684,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my new job i attend a meetings where we discussed how organizations"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5873,
    "model_score": 0.4649,
    "style_score": 0.7097,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was testing a Python application and noticed that some requests were"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4034,
    "model_score": 0.1706,
    "style_score": 0.6362,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Last week I reviewed many database security vulnerablities and some vu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3835,
    "model_score": 0.1181,
    "style_score": 0.6488,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my opinion testing is an important part of as SDLC part because app"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4145,
    "model_score": 0.1796,
    "style_score": 0.6494,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "During my Masters thesis research i created charts/graphs to compare v"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3669,
    "model_score": 0.0565,
    "style_score": 0.6773,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was learning about AI security in terms of policies GRC part and how"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3359,
    "model_score": 0.0133,
    "style_score": 0.6586,
    "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
    "sent": "From Last two days even today i working on flask application as i enab"
  }
]
```

### label coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.424,
    "model_score": 0.1598,
    "style_score": 0.6882,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Yesterday i was working on my thesis project of my masters so i spent "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4129,
    "model_score": 0.1149,
    "style_score": 0.7109,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I had problem understanding one of the codepath assignments at first a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3703,
    "model_score": 0.0923,
    "style_score": 0.6483,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "My Laptop was running slowly when I opened a multiple excel file simul"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.1759,
    "style_score": 0.6684,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my new job i attend a meetings where we discussed how organizations"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5873,
    "model_score": 0.4649,
    "style_score": 0.7097,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was testing a Python application and noticed that some requests were"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4034,
    "model_score": 0.1706,
    "style_score": 0.6362,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Last week I reviewed many database security vulnerablities and some vu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3835,
    "model_score": 0.1181,
    "style_score": 0.6488,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my opinion testing is an important part of as SDLC part because app"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4145,
    "model_score": 0.1796,
    "style_score": 0.6494,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "During my Masters thesis research i created charts/graphs to compare v"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3669,
    "model_score": 0.0565,
    "style_score": 0.6773,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was learning about AI security in terms of policies GRC part and how"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3359,
    "model_score": 0.0133,
    "style_score": 0.6586,
    "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
    "sent": "From Last two days even today i working on flask application as i enab"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5901,
    "model_score": 0.5657,
    "style_score": 0.6146,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Artificial intelligence has fundamentally transformed modern computing"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.558,
    "model_score": 0.6129,
    "style_score": 0.5032,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Cybersecurity represents a critical component of modern digital infras"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6062,
    "model_score": 0.5995,
    "style_score": 0.613,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Machine learning algorithms identify patterns within structured and un"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5623,
    "model_score": 0.528,
    "style_score": 0.5965,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Database management systems provide essential mechanisms for storing, "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6691,
    "model_score": 0.7127,
    "style_score": 0.6255,
    "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
    "sent": "Effective risk management requires a systematic approach to identifyin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5832,
    "model_score": 0.5294,
    "style_score": 0.637,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The integration of artificial intelligence into enterprise environment"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3971,
    "model_score": 0.1863,
    "style_score": 0.6079,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Organizations should establish robust monitoring procedures, implement"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5886,
    "model_score": 0.5355,
    "style_score": 0.6417,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Natural language processing enables computational systems to interpret"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5393,
    "model_score": 0.4709,
    "style_score": 0.6076,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Software quality assurance involves systematic testing methodologies d"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5012,
    "model_score": 0.4099,
    "style_score": 0.5925,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Responsible artificial intelligence development requires transparency,"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4796,
    "model_score": 0.3607,
    "style_score": 0.5985,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I think AI is useful, but sometimes it gives answers that sound correc"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4853,
    "model_score": 0.4594,
    "style_score": 0.5112,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The system processed the request successfully. However, the resulting "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.397,
    "model_score": 0.5885,
    "style_score": 0.2054,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Today was busy. I worked on my assignment, attended a meeting, and fix"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3554,
    "model_score": 0.1265,
    "style_score": 0.5842,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Artificial intelligence can support productivity, although human revie"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4028,
    "model_score": 0.373,
    "style_score": 0.4326,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I opened the application and tried submitting the same text twice. The"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3977,
    "model_score": 0.1797,
    "style_score": 0.6158,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Security testing helps teams find problems before attackers exploit th"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4108,
    "model_score": 0.1675,
    "style_score": 0.6542,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The experiment evaluated multiple samples to determine whether the cla"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6641,
    "model_score": 0.8728,
    "style_score": 0.4554,
    "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
    "sent": "My first attempt failed because the server was not responding. I resta"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3805,
    "model_score": 0.1643,
    "style_score": 0.5968,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Automated systems can improve consistency, but their outputs still req"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5542,
    "model_score": 0.5519,
    "style_score": 0.5566,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I spent an hour debugging a Python script. The problem turned out to b"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.424,
    "model_score": 0.1598,
    "style_score": 0.6882,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Yesterday i was working on my thesis project of my masters so i spent "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4129,
    "model_score": 0.1149,
    "style_score": 0.7109,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I had problem understanding one of the codepath assignments at first a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3703,
    "model_score": 0.0923,
    "style_score": 0.6483,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "My Laptop was running slowly when I opened a multiple excel file simul"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.1759,
    "style_score": 0.6684,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my new job i attend a meetings where we discussed how organizations"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5873,
    "model_score": 0.4649,
    "style_score": 0.7097,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was testing a Python application and noticed that some requests were"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4034,
    "model_score": 0.1706,
    "style_score": 0.6362,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Last week I reviewed many database security vulnerablities and some vu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3835,
    "model_score": 0.1181,
    "style_score": 0.6488,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my opinion testing is an important part of as SDLC part because app"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4145,
    "model_score": 0.1796,
    "style_score": 0.6494,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "During my Masters thesis research i created charts/graphs to compare v"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3669,
    "model_score": 0.0565,
    "style_score": 0.6773,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was learning about AI security in terms of policies GRC part and how"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3359,
    "model_score": 0.0133,
    "style_score": 0.6586,
    "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
    "sent": "From Last two days even today i working on flask application as i enab"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5901,
    "model_score": 0.5657,
    "style_score": 0.6146,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Artificial intelligence has fundamentally transformed modern computing"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.558,
    "model_score": 0.6129,
    "style_score": 0.5032,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Cybersecurity represents a critical component of modern digital infras"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6062,
    "model_score": 0.5995,
    "style_score": 0.613,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Machine learning algorithms identify patterns within structured and un"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5623,
    "model_score": 0.528,
    "style_score": 0.5965,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Database management systems provide essential mechanisms for storing, "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6691,
    "model_score": 0.7127,
    "style_score": 0.6255,
    "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
    "sent": "Effective risk management requires a systematic approach to identifyin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5832,
    "model_score": 0.5294,
    "style_score": 0.637,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The integration of artificial intelligence into enterprise environment"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3971,
    "model_score": 0.1863,
    "style_score": 0.6079,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Organizations should establish robust monitoring procedures, implement"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5886,
    "model_score": 0.5355,
    "style_score": 0.6417,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Natural language processing enables computational systems to interpret"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5393,
    "model_score": 0.4709,
    "style_score": 0.6076,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Software quality assurance involves systematic testing methodologies d"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5012,
    "model_score": 0.4099,
    "style_score": 0.5925,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Responsible artificial intelligence development requires transparency,"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4796,
    "model_score": 0.3607,
    "style_score": 0.5985,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I think AI is useful, but sometimes it gives answers that sound correc"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4853,
    "model_score": 0.4594,
    "style_score": 0.5112,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The system processed the request successfully. However, the resulting "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.397,
    "model_score": 0.5885,
    "style_score": 0.2054,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Today was busy. I worked on my assignment, attended a meeting, and fix"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3554,
    "model_score": 0.1265,
    "style_score": 0.5842,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Artificial intelligence can support productivity, although human revie"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4028,
    "model_score": 0.373,
    "style_score": 0.4326,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I opened the application and tried submitting the same text twice. The"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3977,
    "model_score": 0.1797,
    "style_score": 0.6158,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Security testing helps teams find problems before attackers exploit th"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4108,
    "model_score": 0.1675,
    "style_score": 0.6542,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The experiment evaluated multiple samples to determine whether the cla"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6641,
    "model_score": 0.8728,
    "style_score": 0.4554,
    "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
    "sent": "My first attempt failed because the server was not responding. I resta"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3805,
    "model_score": 0.1643,
    "style_score": 0.5968,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Automated systems can improve consistency, but their outputs still req"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5542,
    "model_score": 0.5519,
    "style_score": 0.5566,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I spent an hour debugging a Python script. The problem turned out to b"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.424,
    "model_score": 0.1598,
    "style_score": 0.6882,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Yesterday i was working on my thesis project of my masters so i spent "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4129,
    "model_score": 0.1149,
    "style_score": 0.7109,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I had problem understanding one of the codepath assignments at first a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3703,
    "model_score": 0.0923,
    "style_score": 0.6483,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "My Laptop was running slowly when I opened a multiple excel file simul"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.1759,
    "style_score": 0.6684,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my new job i attend a meetings where we discussed how organizations"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5873,
    "model_score": 0.4649,
    "style_score": 0.7097,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was testing a Python application and noticed that some requests were"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4034,
    "model_score": 0.1706,
    "style_score": 0.6362,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Last week I reviewed many database security vulnerablities and some vu"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3835,
    "model_score": 0.1181,
    "style_score": 0.6488,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "In my opinion testing is an important part of as SDLC part because app"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4145,
    "model_score": 0.1796,
    "style_score": 0.6494,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "During my Masters thesis research i created charts/graphs to compare v"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3669,
    "model_score": 0.0565,
    "style_score": 0.6773,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I was learning about AI security in terms of policies GRC part and how"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3359,
    "model_score": 0.0133,
    "style_score": 0.6586,
    "label": "Our automated analysis suggests this writing may be human-written. This result is not a guarantee.",
    "sent": "From Last two days even today i working on flask application as i enab"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5901,
    "model_score": 0.5657,
    "style_score": 0.6146,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Artificial intelligence has fundamentally transformed modern computing"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.558,
    "model_score": 0.6129,
    "style_score": 0.5032,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Cybersecurity represents a critical component of modern digital infras"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6062,
    "model_score": 0.5995,
    "style_score": 0.613,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Machine learning algorithms identify patterns within structured and un"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5623,
    "model_score": 0.528,
    "style_score": 0.5965,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Database management systems provide essential mechanisms for storing, "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6691,
    "model_score": 0.7127,
    "style_score": 0.6255,
    "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
    "sent": "Effective risk management requires a systematic approach to identifyin"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5832,
    "model_score": 0.5294,
    "style_score": 0.637,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The integration of artificial intelligence into enterprise environment"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3971,
    "model_score": 0.1863,
    "style_score": 0.6079,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Organizations should establish robust monitoring procedures, implement"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5886,
    "model_score": 0.5355,
    "style_score": 0.6417,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Natural language processing enables computational systems to interpret"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5393,
    "model_score": 0.4709,
    "style_score": 0.6076,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Software quality assurance involves systematic testing methodologies d"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5012,
    "model_score": 0.4099,
    "style_score": 0.5925,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Responsible artificial intelligence development requires transparency,"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4796,
    "model_score": 0.3607,
    "style_score": 0.5985,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I think AI is useful, but sometimes it gives answers that sound correc"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4853,
    "model_score": 0.4594,
    "style_score": 0.5112,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The system processed the request successfully. However, the resulting "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.397,
    "model_score": 0.5885,
    "style_score": 0.2054,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Today was busy. I worked on my assignment, attended a meeting, and fix"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3554,
    "model_score": 0.1265,
    "style_score": 0.5842,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Artificial intelligence can support productivity, although human revie"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4028,
    "model_score": 0.373,
    "style_score": 0.4326,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I opened the application and tried submitting the same text twice. The"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3977,
    "model_score": 0.1797,
    "style_score": 0.6158,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Security testing helps teams find problems before attackers exploit th"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4108,
    "model_score": 0.1675,
    "style_score": 0.6542,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "The experiment evaluated multiple samples to determine whether the cla"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6641,
    "model_score": 0.8728,
    "style_score": 0.4554,
    "label": "Our automated analysis found patterns associated with AI-generated writing. This is not proof of AI use. You can appeal this result.",
    "sent": "My first attempt failed because the server was not responding. I resta"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3805,
    "model_score": 0.1643,
    "style_score": 0.5968,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "Automated systems can improve consistency, but their outputs still req"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5542,
    "model_score": 0.5519,
    "style_score": 0.5566,
    "label": "Our automated analysis cannot reliably determine how this writing was created. No conclusion about AI use should be drawn from this result.",
    "sent": "I spent an hour debugging a Python script. The problem turned out to b"
  }
]
```

### bad input handling

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_02\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_03\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_04\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": [], \"creator_id\": \"eval_bad_05\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": {}, \"creator_id\": \"eval_bad_06\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": true, \"creator_id\": \"eval_bad_07\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   "
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": [\"hello\", \"world\"], \"creator_id\": \"eval_bad_10\"}"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_02\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_03\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_04\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": [], \"creator_id\": \"eval_bad_05\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": {}, \"creator_id\": \"eval_bad_06\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": true, \"creator_id\": \"eval_bad_07\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   "
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": [\"hello\", \"world\"], \"creator_id\": \"eval_bad_10\"}"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_02\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_03\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_04\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": [], \"creator_id\": \"eval_bad_05\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": {}, \"creator_id\": \"eval_bad_06\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": true, \"creator_id\": \"eval_bad_07\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   "
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": [\"hello\", \"world\"], \"creator_id\": \"eval_bad_10\"}"
  }
]
```
