from flask import Blueprint, request, jsonify, Response
from datetime import datetime, timezone

health_bp = Blueprint("health", "health_bp")

@health_bp.route("/health", methods=['GET'])
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "url-shortener-v2",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
