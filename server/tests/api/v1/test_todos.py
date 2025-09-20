from fastapi.testclient import TestClient


def test_post_and_get_todo(client: TestClient):
    # Test initial todos list is empty.
    response = client.get("/api/v1/todo/")
    assert response.status_code == 200
    assert response.json() == []

    # Test posting a new todo.
    new_todo_data = {"text": "Solve the Navier-Stokes existence and smoothness problem."}
    response = client.post("/api/v1/todo/", json=new_todo_data)
    assert response.status_code == 200
    created_todo = response.json()
    assert created_todo["text"] == new_todo_data["text"]
    assert "id" in created_todo

    # Get the newly created todo.
    response = client.get("/api/v1/todo/")
    assert response.status_code == 200
    todos = response.json()
    assert any(todo["id"] == created_todo["id"] and todo["text"] == new_todo_data["text"] for todo in todos)

    # Create another todo.
    second_todo_data = {"text": "Solve the Riemann Hypothesis."}
    response = client.post("/api/v1/todo/", json=second_todo_data)
    assert response.status_code == 200
    second_created_todo = response.json()
    assert second_created_todo["text"] == second_todo_data["text"]
    assert "id" in second_created_todo

    # Get both created todos.
    response = client.get("/api/v1/todo/")
    assert response.status_code == 200
    todos = response.json()
    todo_texts = {todo["text"] for todo in todos}
    assert new_todo_data["text"] in todo_texts
    assert second_todo_data["text"] in todo_texts
    assert len(todos) > 1
