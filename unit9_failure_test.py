from unittest.mock import patch
from app import app

client = app.test_client()

with patch("request_logging.record_request", side_effect=OSError("Simulated disk error")):
    response = client.post("/ping", json={"message": "test"})
    print("HTTP STATUS:", response.status_code)
    print("EXPECTED: 200")
    print("IMPROVEMENT:", "PASS" if response.status_code == 200 else "FAIL")
