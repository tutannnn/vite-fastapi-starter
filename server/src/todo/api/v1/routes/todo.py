"""Defines the API endpoints for version 1 of the application."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from todo.api.v1.schemas.todo import TodoCreate, TodoRead
from todo.api.v1.services.todo import TodoService
from todo.db.session import get_db

router = APIRouter()


def get_todo_service() -> TodoService:
    """Returns an instance of the todo service.

    Returns:
        TodoService: An instance of the todo service.
    """
    return TodoService()


@router.get("/")
def list_todos(
    db: Session = Depends(get_db),
    service: TodoService = Depends(get_todo_service),
) -> list[TodoRead]:
    """Returns all todo items from the database.

    Args:
        db (Session, optional): Database session for queries. Defaults to Depends(get_db).
        service (TodoService, optional): Service implementing DB queries. Defaults to Depends(get_todo_service).

    Returns:
        list[TodoRead]: All todo items from the database.
    """
    return service.get_all_todos(db)


@router.post("/")
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    service: TodoService = Depends(get_todo_service),
) -> TodoRead:
    """Inserts a new todo item into the database.

    Args:
        todo (TodoCreate): New todo item data.
        db (Session, optional): Database session for insertions. Defaults to Depends(get_db).
        service (TodoService, optional): Service implementing DB insertions. Defaults to Depends(get_todo_service).

    Returns:
        TodoRead: Newly created todo item from the DB.
    """
    return service.create_todo(todo, db)
