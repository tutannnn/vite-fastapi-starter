import uuid

import pytest
from httpx import AsyncClient, Response

from tests.conftest import auth_headers


async def signup_user(client: AsyncClient, username: str) -> Response:
    return await client.post("/api/v1/auth/signup", json={"username": username})


@pytest.mark.anyio
async def test_signup(client: AsyncClient):
    username = f"Euler_{uuid.uuid4().hex[:6]}"
    response = await signup_user(client, username)
    assert response.status_code == 200
    user = response.json()
    assert user["username"] == username
    assert "id" in user


@pytest.mark.anyio
async def test_login(client: AsyncClient):
    username = f"Gauss_{uuid.uuid4().hex[:6]}"
    await signup_user(client, username)

    response = await client.post("/api/v1/auth/login", json={"username": username})
    assert response.status_code == 200
    user = response.json()
    assert user["username"] == username


@pytest.mark.anyio
async def test_get_me(client: AsyncClient):
    username = f"Erdos_{uuid.uuid4().hex[:6]}"
    signup_resp = await signup_user(client, username)
    user_id = signup_resp.json()["id"]

    response = await client.get("/api/v1/auth/me", headers=auth_headers(user_id))
    assert response.status_code == 200
    assert response.json()["username"] == username
