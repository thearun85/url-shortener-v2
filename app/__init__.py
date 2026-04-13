import logging
from flask import Flask
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
