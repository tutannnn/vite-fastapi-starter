import uuid
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session, sessionmaker

from todo.db.base import Base
from todo.db.models.user import User
from todo.db.session import get_db
from todo.main import app

# Use local SQLite file for unit tests.
TEST_DB_URI = "sqlite:///:memory:"

engine = create_engine(TEST_DB_URI, connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module", autouse=True)
def setup_test_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def auth_headers(user_id: int):
    return {"Authorization": f"Bearer {user_id}"}


@pytest.fixture
def db() -> Generator[Session]:
    yield from override_get_db()


@pytest.fixture
def test_user(db: Session) -> User:
    username = f"test_{uuid.uuid4().hex[:6]}"
    user = User(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
