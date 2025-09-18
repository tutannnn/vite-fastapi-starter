from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from todo.session import get_db
from todo.models import Todo
from todo.schemas import TodoCreate, TodoRead

router = APIRouter()

@router.get("/", response_model=list[TodoRead])
def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

@router.post("/", response_model=TodoRead)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(text=todo.text)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
