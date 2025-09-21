"""Database model for todo items."""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from todo.db.base import Base


class Todo(Base):
    """Represents a task to be completed."""

    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(30), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped["User"] = relationship(back_populates="todos")  # noqa: F821 # type: ignore

    def __repr__(self) -> str:
        return f"Todo(id={self.id!r}, text={self.text!r})"
