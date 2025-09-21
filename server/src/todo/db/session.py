"""Database session management."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from todo.core.config import settings

engine = create_async_engine(
    settings.db_url,
    echo=True,  # TODO: For SQL debugging in dev.
)

SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
    future=True,
)


async def get_db() -> AsyncGenerator[AsyncSession]:
    """Yields a database session.

    Yields:
        AsyncGenerator[AsyncSession]: A database session scoped to the request lifecycle.
    """
    async with SessionLocal() as session:
        yield session
