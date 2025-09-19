from app.api.v1.schemas.todo import TodoCreate, TodoRead
from app.db.models.todo import Todo
from sqlalchemy.orm import Session


class TodoService:
    @staticmethod
    def get_todos(db: Session):
        todos = db.query(Todo).all()
        return [TodoRead.model_validate(todo) for todo in todos]

    @staticmethod
    def create_todo(todo: TodoCreate, db: Session):
        db_todo = Todo(text=todo.text)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return TodoRead.model_validate(db_todo)
