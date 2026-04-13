import pytest
from flask import Flask
from flask.testing import FlaskClient
from app import create_app

from app.shortcode import CODE_LENGTH

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
    
def test_shorten_returns_shortcode(client: FlaskClient) -> None:
    response = client.post(
        "/shorten",
        json={"url": "https://google.com"},
    )
    assert response.status_code == 201
    data = response.get_json()
    assert "shortcode" in data
    assert len(data["shortcode"]) == CODE_LENGTH

def test_shorten_empty_url_returns_400(client: FlaskClient) -> None:
    response = client.post(
        "/shorten",
        json={"url": ""},
    )
    assert response.status_code == 400
    data = response.get_json()
    data["error"] == "url cannot be empty"

def test_shorten_missing_url_returns_400(client: FlaskClient) -> None:
    response = client.post(
        "/shorten",
        json={},
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "url is required"

def test_shorten_no_body_returns_400(client: FlaskClient) -> None:
    response = client.post(
        "/shorten",
    )
    assert response.status_code == 400
