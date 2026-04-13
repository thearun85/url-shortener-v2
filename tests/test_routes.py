import pytest
from flask import Flask
from flask.testing import FlaskClient
from app import create_app

@pytest.fixture
def app() -> Flask:
    app = create_app()
    app.config["TESTING"] = True
    return app

@pytest.fixture
def flask_client(app: Flask) -> FlaskClient:
    return app.test_client()

def test_health_route(client: FlaskClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "ok"
    assert data['service'] == "url-shortener-v2"
    assert "timestamp" in data
    
