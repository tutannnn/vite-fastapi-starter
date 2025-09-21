"""Services called by the todo router for interacting with the database."""

from fastapi import HTTPException
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from todo.api.v1.schemas.todo import TodoCreate, TodoRead
from todo.db.models.todo import Todo
from todo.db.models.user import User


class TodoService:
    """Services called by the todo router for interacting with the database."""

    @staticmethod
    async def get_all_todos(db: AsyncSession, user: User) -> list[TodoRead]:
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

        stmt = select(Todo).filter(Todo.user_id == user.id).order_by(Todo.id)
        result = await db.execute(stmt)
        todos = result.scalars().all()

        logger.info(
            "Fetched todos successfuly",
            extra={
                "len_todos": len(todos),
            },
        )

        return [TodoRead.model_validate(todo) for todo in todos]

    @staticmethod
    async def create_todo(db: AsyncSession, todo: TodoCreate, user: User) -> TodoRead:
        """Creates a new todo item in the database.

        Args:
            db (AsyncSession): Database session for insertions.
            todo (TodoCreate): Input data for the new todo.
            user (User): Authenticated user from the DB.

        Returns:
            TodoRead: Todo item inserted into the database.
        """
        logger.info("Creating new todo", extra={"user_id": user.id, "text_snippet": todo.text[:30]})

        new_todo = Todo(text=todo.text, user_id=user.id)
        db.add(new_todo)
        await db.commit()
        await db.refresh(new_todo)

        logger.info(
            "Created todo successfully",
            extra={
                "todo_id": new_todo.id,
                "user_id": user.id,
            },
        )

        return TodoRead.model_validate(new_todo)

    @staticmethod
    async def delete_todo(todo_id: int, db: AsyncSession, user: User) -> None:
        """Deletes a todo if it exists and belongs to the user.

        Args:
            todo_id (int): ID of the todo to delete.
            db (AsyncSession): DB session for deletions.
            user (User): Authenticated user.

        Raises:
            HTTPException: 404 if todo not found or not owned by user.
        """
        stmt = select(Todo).filter_by(id=todo_id, user_id=user.id)
        result = await db.execute(stmt)
        todo = result.scalars().first()

        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")

        await db.delete(todo)
        await db.commit()
