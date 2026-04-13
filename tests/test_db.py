import pytest
from flask import Flask
from sqlalchemy import text

from app import create_app

@pytest.fixture
def app() -> Flask:
    app = create_app()
    app.config["TESTING"] = True
    return app

def test_db(app: Flask) -> None:
    session_factory = app.config["SESSION_FACTORY"]
    with session_factory() as session:
        result = session.execute(text("SELECT 1"))
        assert result.scalar() == 1
