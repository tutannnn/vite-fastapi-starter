"""Database model for todo items."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from todo.db.base import Base


class Todo(Base):
    """Represents a task to be completed."""

    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(30), nullable=False)

    def __repr__(self) -> str:
        return f"Todo(id={self.id!r}, text={self.text!r})"
