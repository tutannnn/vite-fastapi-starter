"""Database model for user metadata and authentication."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from todo.db.base import Base


class User(Base):
    """Represents a user of the app."""

    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)

    todos: Mapped[list["Todo"]] = relationship(  # noqa: F821 # type: ignore
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"
