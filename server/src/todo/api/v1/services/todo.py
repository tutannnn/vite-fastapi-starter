"""Services called by the todo router for interacting with the database."""

from loguru import logger
from sqlalchemy.orm import Session

from todo.api.v1.schemas.todo import TodoCreate, TodoRead
from todo.db.models.todo import Todo


class TodoService:
    """Services called by the todo router for interacting with the database."""

    @staticmethod
    def get_all_todos(db: Session) -> list[TodoRead]:
        """Fetches all todo items from the database.

        Args:
            db (Session): Database session for queries.

        Returns:
            list[TodoRead]: All todo items from the database.
        """
        logger.info("Fetching all todos from the DB.")
        todos = db.query(Todo).all()
        logger.info("Retrieved %d todos from the DB.", len(todos))
        return [TodoRead.model_validate(todo) for todo in todos]

    @staticmethod
    def create_todo(todo: TodoCreate, db: Session) -> TodoRead:
        """Creates a new todo item in the database.

        Args:
            todo (TodoCreate): Input data for the new todo.
            db (Session): Database session for insertions.

        Returns:
            TodoRead: Todo item inserted into the database.
        """
        logger.info("Creating todo with content: %s", todo.text)
        new_todo = Todo(text=todo.text)
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        logger.info("Created todo with ID: %d", new_todo.id)
        return TodoRead.model_validate(new_todo)
