from fastapi.testclient import TestClient
from httpx import Response

from tests.conftest import auth_headers


def signup_user(client: TestClient, username: str) -> Response:
    return client.post("/api/v1/auth/signup", json={"username": username})


def test_signup(client: TestClient):
    username = "Euler"
    response = signup_user(client, username)
    assert response.status_code == 200
    user = response.json()
    assert user["username"] == username
    assert "id" in user


def test_login(client: TestClient):
    username = "Gauss"
    signup_user(client, username)

    response = client.post("/api/v1/auth/login", json={"username": username})
    assert response.status_code == 200
    user = response.json()
    assert user["username"] == username


def test_get_me(client: TestClient):
    username = "Erdos"
    signup_resp = signup_user(client, username)
    user_id = signup_resp.json()["id"]

    response = client.get("/api/v1/auth/me", headers=auth_headers(user_id))
    assert response.status_code == 200
    assert response.json()["username"] == username
