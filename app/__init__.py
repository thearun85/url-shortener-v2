import logging
from flask import Flask
from datetime import datetime, timezone

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/health", methods=['GET'])
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "service": "url-shortener-v2",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    return app
