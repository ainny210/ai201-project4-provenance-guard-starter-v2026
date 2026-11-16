import json
from pathlib import Path
from statistics import mean

baseline = json.loads(Path("results/unit9_baseline.json").read_text())
after = json.loads(Path("results/unit9_after.json").read_text())

logs = [
    json.loads(line)
    for line in Path("logs/unit9_requests.jsonl").read_text().splitlines()
    if line.strip()
]

successes = [x for x in logs if x["status_code"] == 200]
rejections = [x for x in logs if x["status_code"] >= 400]
pings = [
    x for x in successes
    if x["endpoint"] == "/ping"
][-10:]

if len(successes) < 5 or len(rejections) < 5 or len(pings) < 10:
    raise SystemExit("Insufficient real logs.")

sample = successes[-5:] + rejections[-5:]

def met_count(data, criterion):
    return sum(trial[criterion]["met"] for trial in data)

criteria = ["C1", "C2", "C3", "C4", "C5"]

rows = "\n".join(
    f"| {c} | {met_count(baseline, c)}/3 | {met_count(after, c)}/3 |"
    for c in criteria
)

avg = mean(x["duration_ms"] for x in pings)
daily = avg * 100

sample_text = "\n".join(json.dumps(x) for x in sample)

report = f"""
**Instrumentation**

The Flask service records UTC timestamps, request methods, endpoints,
HTTP status codes, processing durations, text-length metadata, and
rejection flags in `logs/unit9_requests.jsonl`.

Full submitted text is not included.

Ten actual request log entries:

```jsonl
{sample_text}
```

**What It Costs**
Ten successful /ping requests were measured.

Average processing time: {avg:.3f} milliseconds.

For 100 requests/day:

{avg:.3f} ms × 100 = {daily:.3f} ms/day
= {daily / 1000:.6f} seconds/day.

This measures lightweight /ping processing only, not GPT-2 inference
or concurrent production traffic.

Additional cloud hosting cost: $0 because the application runs locally.
Hardware, electricity, and development time are excluded.

The GPT-2 download is approximately 550 MB. PyTorch also requires
substantial memory, making a 512 MB free hosting instance unsuitable.

**Run Log and Verdicts**

Five criteria were tested three times before and after improvement.

| Criterion | Baseline | Final |
|---|---:|---:|
{rows}		

C1: Complete structured request logs.
C2: /ping processing below 50 ms.
C3: Invalid requests rejected and logged.
C4: Expected responses without unexpected HTTP 500 errors.
C5: Metadata logging without storing submitted text.

Evidence:

criteria.md
results/unit9_baseline.json
results/unit9_after.json
results/unit9_log_sample.jsonl

**The Improvement**

I added exception handling around the structured request logger.
If writing a log raises OSError, Flask records the error without
interrupting the original HTTP response.

I verified this by injecting a simulated disk error using
unit9_failure_test.py. The /ping endpoint still returned HTTP 200.

One baseline C4 trial also failed. The evaluation harness was updated
to generate unique creator IDs to avoid unintended rate-limit
interactions. The improved C4 result cannot be attributed solely
to the application change.

**What's Still Broken**

Logging failures can cause individual log entries to be lost.
JSONL logs have no automatic rotation or centralized collection.
The Flask development server is not production-ready.
The benchmark does not measure GPT-2 inference or concurrency.
The AI detector may still produce false positives.
In-memory rate-limit state does not survive restarts.

**How I Used AI**

I used AI assistance to implement structured Flask request logging.
I verified its output by inspecting real JSONL records.
I used AI assistance to create acceptance tests and investigate
a failed reliability trial. I checked the explanations against
actual test results.
I used AI assistance to create a simulated disk-error test.
I ran it locally and confirmed that /ping still returned HTTP 200.
"""

readme = Path("README.md")
content = readme.read_text(encoding="utf-8")

# Preserve the existing Capstone introduction and its first three labels.
if "**Instrumentation**" in content.split("## Capstone")[-1]:
    content = content.rsplit("**Instrumentation**", 1)[0]

readme.write_text(content.rstrip() + "\n\n" + report, encoding="utf-8")

Path("results/unit9_log_sample.jsonl").write_text(
    sample_text + "\n", encoding="utf-8"
)

print("README Capstone completed.")
print("Real log entries included:", len(sample))
print("Average /ping processing time:", round(avg, 3), "ms")
print("Baseline:", [met_count(baseline, c) for c in criteria])
print("Final:", [met_count(after, c) for c in criteria])