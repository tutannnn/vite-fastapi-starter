from sqlalchemy.orm import Session

from todo.api.v1.schemas import TodoCreate
from todo.models import Todo


class TodoService:
    @staticmethod
    def get_todos(db: Session):
        return db.query(Todo).all()

    @staticmethod
    def create_todo(todo: TodoCreate, db: Session):
        db_todo = Todo(text=todo.text)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo
