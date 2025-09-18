from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from todo.api.v1.schemas import TodoCreate, TodoRead
from todo.api.v1.service import TodoService
from todo.session import get_db

router = APIRouter()
service = TodoService()


@router.get("/", response_model=list[TodoRead])
def get_todos(db: Session = Depends(get_db)):
    return service.get_todos(db)


@router.post("/", response_model=TodoRead)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return service.create_todo(todo, db)
