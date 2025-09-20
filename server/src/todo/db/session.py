"""Database session management."""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from todo.core.config import settings

engine = create_engine(
    settings.db_url,
    echo=True,  # TODO: For SQL debugging in dev.
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)


def get_db() -> Generator[Session]:
    """Yields a database session.

    Yields:
        Session: A database session scoped to the request lifecycle.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
