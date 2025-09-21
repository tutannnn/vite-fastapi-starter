import pytest
from httpx import AsyncClient

from tests.conftest import auth_headers
from todo.db.models.user import User


@pytest.mark.anyio
async def test_post_and_get_todo(client: AsyncClient, test_user: User):
    # Test that user authentication is required for the todo endpoint.
    response = await client.get("/api/v1/todo/")
    assert response.status_code == 403

    headers = auth_headers(test_user.id)

    # Test initial todos list is empty.
    response = await client.get("/api/v1/todo/", headers=headers)
    assert response.status_code == 200
    assert response.json() == []

    # Test posting a new todo.
    new_todo_data = {"text": "Solve the Navier-Stokes existence and smoothness problem."}
    response = await client.post("/api/v1/todo/", headers=headers, json=new_todo_data)
    assert response.status_code == 200
    created_todo = response.json()
    assert created_todo["text"] == new_todo_data["text"]
    assert "id" in created_todo

    # Get the newly created todo.
    response = await client.get("/api/v1/todo/", headers=headers)
    assert response.status_code == 200
    todos = response.json()
    assert any(todo["id"] == created_todo["id"] and todo["text"] == new_todo_data["text"] for todo in todos)

    # Create another todo.
    second_todo_data = {"text": "Solve the Riemann Hypothesis."}
    response = await client.post("/api/v1/todo/", headers=headers, json=second_todo_data)
    assert response.status_code == 200
    second_created_todo = response.json()
    assert second_created_todo["text"] == second_todo_data["text"]
    assert "id" in second_created_todo

    # Get both created todos.
    response = await client.get("/api/v1/todo/", headers=headers)
    assert response.status_code == 200
    todos = response.json()
    todo_texts = {todo["text"] for todo in todos}
    assert new_todo_data["text"] in todo_texts
    assert second_todo_data["text"] in todo_texts
    assert len(todos) > 1


@pytest.mark.anyio
async def test_delete_todo(client: AsyncClient, test_user: User):
    # Create todo.
    headers = auth_headers(test_user.id)
    todo_data = {"text": "Solve the P versus NP problem."}
    create_resp = await client.post("/api/v1/todo/", json=todo_data, headers=headers)
    todo_id = create_resp.json()["id"]

    # Delete it.
    delete_resp = await client.delete(f"/api/v1/todo/{todo_id}", headers=headers)
    assert delete_resp.status_code == 204

    get_resp = await client.get("/api/v1/todo/", headers=headers)
    assert all(todo["id"] != todo_id for todo in get_resp.json())
