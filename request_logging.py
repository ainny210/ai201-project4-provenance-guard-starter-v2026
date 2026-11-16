import json
import threading
from datetime import datetime, timezone
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent / "logs" / "unit9_requests.jsonl"
LOCK = threading.Lock()

def record_request(method, endpoint, status_code, duration_ms, text_length, rejected):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "method": method,
        "endpoint": endpoint,
        "status_code": status_code,
        "duration_ms": round(duration_ms, 3),
        "input_metadata": {"text_length": text_length},
        "output": {"status_code": status_code},
        "rejected": rejected
    }
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOCK:
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
