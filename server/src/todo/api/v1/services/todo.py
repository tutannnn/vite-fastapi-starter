"""Services called by the todo router for interacting with the database."""

from loguru import logger
from sqlalchemy.orm import Session

from todo.api.v1.schemas.todo import TodoCreate, TodoRead
from todo.db.models.todo import Todo
from todo.db.models.user import User


class TodoService:
    """Services called by the todo router for interacting with the database."""

    @staticmethod
    def get_all_todos(db: Session, user: User) -> list[TodoRead]:
        """Fetches all todo items from the database for a given user.

        Args:
            db (Session): Database session for queries.
            user (User): Authenticated user from the DB.

        Returns:
            list[TodoRead]: All todo items from the database.
        """
        logger.info(
            "Fetching todos",
            extra={
                "user_id": user.id,
            },
        )

        todos = db.query(Todo).filter(Todo.user_id == user.id).all()

        logger.info(
            "Fetched todos successfuly",
            extra={
                "len_todos": len(todos),
            },
        )

        return [TodoRead.model_validate(todo) for todo in todos]

    @staticmethod
    def create_todo(db: Session, todo: TodoCreate, user: User) -> TodoRead:
        """Creates a new todo item in the database.

        Args:
            db (Session): Database session for insertions.
            todo (TodoCreate): Input data for the new todo.
            user (User): Authenticated user from the DB.

        Returns:
            TodoRead: Todo item inserted into the database.
        """
        logger.info("Creating new todo", extra={"user_id": user.id, "text_snippet": todo.text[:30]})

        new_todo = Todo(text=todo.text, user_id=user.id)
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)

        logger.info(
            "Created todo successfully",
            extra={
                "todo_id": new_todo.id,
                "user_id": user.id,
            },
        )

        return TodoRead.model_validate(new_todo)
