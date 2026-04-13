import logging
import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime, timezone
from dotenv import load_dotenv

from .models import Base

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app() -> Flask:
    app = Flask(__name__)
    db_url: str = os.environ["DATABASE_URL"]
    engine = create_engine(db_url)
    app.config["SESSION_FACTORY"] = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)
    logger.info("Database tables created..")
    
    @app.route("/health", methods=['GET'])
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "service": "url-shortener-v2",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    logger.info("App created.")
    return app
