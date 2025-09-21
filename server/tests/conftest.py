import uuid
from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from todo.db.base import Base
from todo.db.models.user import User
from todo.db.session import get_db
from todo.main import app

# Use local SQLite file for unit tests.
TEST_DB_URI = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(TEST_DB_URI, connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)


async def override_get_db() -> AsyncGenerator[AsyncSession]:
    async with TestingSessionLocal() as session:
        yield session


app.dependency_overrides[get_db] = override_get_db


@pytest_asyncio.fixture(scope="module", autouse=True)
async def setup_test_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture
async def db() -> AsyncGenerator[AsyncSession]:
    async with TestingSessionLocal() as session:
        yield session


@pytest.fixture(scope="module")
async def client() -> AsyncGenerator[AsyncClient]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c


def auth_headers(user_id: int):
    return {"Authorization": f"Bearer {user_id}"}


@pytest_asyncio.fixture
async def test_user(db: AsyncSession) -> User:
    username = f"test_{uuid.uuid4().hex[:6]}"
    user = User(username=username)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
