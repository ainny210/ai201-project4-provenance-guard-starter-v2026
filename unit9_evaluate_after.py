import uuid
import json
import statistics
from pathlib import Path
from app import app
from request_logging import LOG_FILE

client = app.test_client()
results = []

invalid = [
    {},
    {"text": ""},
    {"text": 123},
    {"text": "a"},
    {"text": "x" * 10001},
]

def ping():
    return client.post("/ping", json={"message": "unit9"})

def bad_submit(i):
    payload = dict(invalid[i % 5])
    payload["creator_id"] = "unit9-" + str(uuid.uuid4())
    return client.post("/submit", json=payload)

def read_new(start):
    lines = LOG_FILE.read_text(encoding="utf-8-sig").splitlines()
    return [json.loads(x) for x in lines[start:]]

def run_trial(number):
    trial = {}

    # Criterion 1: 5 ping + 5 invalid submissions
    start = len(LOG_FILE.read_text(encoding="utf-8-sig").splitlines())
    responses = [ping() for _ in range(5)]
    responses += [bad_submit(i) for i in range(5)]
    entries = read_new(start)
    required = ("timestamp", "method", "endpoint", "status_code", "duration_ms")
    count = sum(all(k in e for k in required) for e in entries)
    trial["C1"] = {"value": count, "target": 10, "met": count == 10 and len(entries) == 10}

    # Criterion 2: 10 ping requests
    start = len(LOG_FILE.read_text(encoding="utf-8-sig").splitlines())
    for _ in range(10):
        ping()
    entries = read_new(start)
    average = statistics.mean(e["duration_ms"] for e in entries)
    trial["C2"] = {"value": round(average, 3), "target": "<50 ms", "met": len(entries) == 10 and average < 50}

    # Criterion 3: 10 invalid submissions
    start = len(LOG_FILE.read_text(encoding="utf-8-sig").splitlines())
    responses = [bad_submit(i) for i in range(10)]
    entries = read_new(start)
    passed = sum(
        r.status_code in (400, 413) and e["rejected"]
        for r, e in zip(responses, entries)
    )
    trial["C3"] = {"value": passed, "target": 10, "met": passed == 10 and len(entries) == 10}

    # Criterion 4: 5 ping + 5 invalid submissions
    responses = [ping() for _ in range(5)]
    responses += [bad_submit(i) for i in range(5)]
    passed = sum(r.status_code == 200 for r in responses[:5])
    passed += sum(r.status_code in (400, 413) for r in responses[5:])
    trial["C4"] = {"value": passed, "target": 10, "met": passed == 10}

    # Criterion 5: 10 invalid /submit requests
    start = len(LOG_FILE.read_text(encoding="utf-8-sig").splitlines())
    for i in range(10):
        bad_submit(i)
    entries = read_new(start)
    required = ("timestamp", "status_code", "duration_ms", "input_metadata")
    passed = sum(
        all(k in e for k in required)
        and "text_length" in e["input_metadata"]
        and "text" not in e
        for e in entries
    )
    trial["C5"] = {"value": passed, "target": 10, "met": passed == 10 and len(entries) == 10}

    return trial

if not LOG_FILE.exists():
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    LOG_FILE.touch()

for n in range(1, 4):
    result = run_trial(n)
    results.append(result)
    print("\nTRIAL", n)
    for criterion, data in result.items():
        verdict = "MET" if data["met"] else "MISSED"
        print(criterion, "=", data["value"], "|", verdict)

output = Path("results/unit9_after.json")
output.parent.mkdir(exist_ok=True)
output.write_text(json.dumps(results, indent=2), encoding="utf-8")

print("\nBASELINE SAVED:", output)
