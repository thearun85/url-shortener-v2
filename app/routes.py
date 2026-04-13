import logging
from datetime import UTC, datetime

from flask import Blueprint, current_app, jsonify, redirect, request
from flask.typing import ResponseReturnValue

from .models import URL
from .shortcode import generate_shortcode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

health_bp = Blueprint("health", "health_bp")

url_bp = Blueprint("url", "url_bp")


@health_bp.route("/health", methods=["GET"])
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "url-shortener-v2",
        "timestamp": datetime.now(UTC).isoformat(),
    }


@url_bp.route("/shorten", methods=["POST"])
def shorten() -> ResponseReturnValue:
    data = request.get_json(silent=True)
    if not data or "url" not in data:
        return jsonify({"error": "url is required"}), 400

    original_url = data["url"].strip()
    if not original_url:
        return jsonify({"error": "url cannot be empty"}), 400
    session_factory = current_app.config["SESSION_FACTORY"]
    with session_factory() as session:
        existing_url = session.query(URL).filter_by(original_url=original_url).first()
        if existing_url:
            return jsonify(
                {
                    "shortcode": existing_url.shortcode,
                }
            ), 200

        shortcode = generate_shortcode()
        url = URL(
            shortcode=shortcode,
            original_url=original_url,
        )
        session.add(url)
        session.commit()

    logger.info(f"Shortcode {shortcode} created for url {original_url}.")
    return jsonify(
        {
            "shortcode": shortcode,
        }
    ), 201


@url_bp.route("/<code>", methods=["GET"])
def redirect_to_url(code: str) -> ResponseReturnValue:

    session_factory = current_app.config["SESSION_FACTORY"]
    with session_factory() as session:
        url = session.query(URL).filter_by(shortcode=code).first()
        if not url:
            return jsonify(
                {
                    "error": f"invalid shortcode {code}",
                }
            ), 404

        return redirect(url.original_url, 302)
