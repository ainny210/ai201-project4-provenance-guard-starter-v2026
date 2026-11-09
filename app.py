#!/usr/bin/env python3
"""
Provenance Guard - Web Service

Routes:
    POST /ping
    POST /submit
    POST /appeal
    GET  /log
    GET  /health

Unit 8 improvement:
    Reject unsafe short inputs before running the detector.
    Record rejected submissions in the audit log.
"""

import uuid

from flask import Flask, jsonify, request

import audit
import config
import detector
import stylometry
import scoring

app = Flask(__name__)


# ---------------------------------------------------------
# RATE LIMITING
# ---------------------------------------------------------

class _LimiterOff:
    """No-op limiter when rate limiting is disabled."""

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()

if config.RATE_LIMITING_ENABLED:

    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """Apply rate limits per creator when possible."""

        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            return get_remote_address()

        creator = payload.get("creator_id")

        if isinstance(creator, str) and creator.strip():
            return creator

        return get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):

        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            payload = {}

        creator_id = payload.get("creator_id", "unknown")

        if not isinstance(creator_id, str):
            creator_id = "unknown"

        audit.log_rejection(
            creator_id=creator_id,
            reason="rate_limited",
            limit=str(exc.description),
        )

        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ---------------------------------------------------------
# REJECTION LOGGING HELPER
# ---------------------------------------------------------

def reject_submission(creator_id, reason, message, status_code=400):
    """
    Reject invalid input and create an audit entry.

    Uses the existing audit.log_rejection function.
    """

    if not isinstance(creator_id, str) or not creator_id.strip():
        creator_id = "unknown"

    audit.log_rejection(
        creator_id=creator_id,
        reason=reason,
    )

    return jsonify({
        "error": reason,
        "message": message,
    }), status_code


# ---------------------------------------------------------
# PING - ORIGINAL CONTROL ROUTE
# ---------------------------------------------------------

@app.post("/ping")
def ping():

    payload = request.get_json(silent=True) or {}

    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


# ---------------------------------------------------------
# HEALTH
# ---------------------------------------------------------

@app.get("/health")
def health():

    loaded = detector._model is not None

    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ---------------------------------------------------------
# SUBMIT - IMPROVED INPUT VALIDATION
# ---------------------------------------------------------

@app.post("/submit")
@limiter.limit(
    f"{config.RATE_LIMIT_PER_MINUTE}/minute;"
    f"{config.RATE_LIMIT_PER_DAY}/day"
)
def submit():

    payload = request.get_json(silent=True)

    # Reject malformed JSON or non-object payloads.
    if not isinstance(payload, dict):

        return reject_submission(
            creator_id="unknown",
            reason="invalid_json",
            message="Expected a JSON object",
            status_code=400,
        )

    text = payload.get("text")
    creator_id = payload.get("creator_id", "anonymous")

    # Validate creator ID.
    if not isinstance(creator_id, str) or not creator_id.strip():

        return reject_submission(
            creator_id="unknown",
            reason="invalid_creator_id",
            message="creator_id must be a non-empty string",
            status_code=400,
        )

    # Validate text type and empty values.
    if not isinstance(text, str) or not text.strip():

        return reject_submission(
            creator_id=creator_id,
            reason="invalid_text",
            message="text must be a non-empty string",
            status_code=400,
        )

    # -----------------------------------------------------
    # UNIT 8 MEASURED IMPROVEMENT
    #
    # BEFORE:
    # A single-character submission ("a") reached the
    # detector and produced HTTP 500 in attack MF02.
    #
    # AFTER:
    # Reject the request before detector processing.
    # Expected result: HTTP 400 and an audit entry.
    # -----------------------------------------------------

    if len(text.strip()) < 2:

        return reject_submission(
            creator_id=creator_id,
            reason="text_too_short",
            message="text must contain at least 2 characters",
            status_code=400,
        )

    # Reject oversized submissions.
    if len(text) > 10000:

        return reject_submission(
            creator_id=creator_id,
            reason="text_too_long",
            message="text exceeds 10000 characters",
            status_code=413,
        )

    # Generate content ID.
    content_id = str(uuid.uuid4())

    # -----------------------------------------------------
    # DETECTION PIPELINE
    # -----------------------------------------------------

    model_score = float(detector.model_signal(text))

    style_score = float(stylometry.style_signal(text))

    confidence = float(
        scoring.combine_signals(
            model_score,
            style_score,
        )
    )

    confidence = max(
        0.0,
        min(1.0, confidence),
    )

    guess, label = scoring.score_to_label(confidence)

    # -----------------------------------------------------
    # AUDIT DECISION
    # -----------------------------------------------------

    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=confidence,
        label=label,
    )

    # -----------------------------------------------------
    # RESPONSE
    # -----------------------------------------------------

    return jsonify({
        "content_id": content_id,
        "guess": guess,
        "confidence": round(confidence, 4),
        "label": label,
        "model_score": round(model_score, 4),
        "style_score": round(style_score, 4),
    }), 200


# ---------------------------------------------------------
# APPEAL
# ---------------------------------------------------------

@app.post("/appeal")
def appeal():

    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):

        return jsonify({
            "error": "Expected a JSON object"
        }), 400

    content_id = payload.get("content_id")
    reasoning = payload.get("reasoning")

    if not isinstance(content_id, str) or not content_id.strip():

        return jsonify({
            "error": "content_id is required"
        }), 400

    if not isinstance(reasoning, str) or not reasoning.strip():

        return jsonify({
            "error": "reasoning is required"
        }), 400

    entries = audit.entries_for(content_id)

    decisions = [
        entry
        for entry in entries
        if entry.get("status") == "decided"
    ]

    if not decisions:

        return jsonify({
            "error": "Submission not found"
        }), 404

    creator_id = decisions[0]["creator_id"]

    audit.log_appeal(
        content_id=content_id,
        creator_id=creator_id,
        reasoning=reasoning,
    )

    return jsonify({
        "content_id": content_id,
        "status": "under_review",
        "message": "Your appeal has been recorded for human review.",
    }), 200


# ---------------------------------------------------------
# AUDIT LOG
# ---------------------------------------------------------

@app.get("/log")
def get_log():

    limit = request.args.get("limit", type=int)

    entries = audit.read_entries(limit=limit)

    return jsonify({
        "count": len(entries),
        "entries": entries,
    })


# ---------------------------------------------------------
# START APPLICATION
# ---------------------------------------------------------

def main():

    print(
        f"Provenance Guard on "
        f"http://{config.HOST}:{config.PORT}"
    )

    print(f"Detector model: {config.DETECTOR_MODEL}")

    print(
        "Rate limiting:",
        "ON" if config.RATE_LIMITING_ENABLED else "OFF",
    )

    print(f"Audit log: {config.AUDIT_LOG}")

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
    )


if __name__ == "__main__":
    main()