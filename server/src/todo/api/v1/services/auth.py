"""Defines user authentication services.

NOTE: This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from todo.api.v1.schemas.auth import UserCreate, UserRead
from todo.db.models.user import User


class AuthService:
    """Services called by the auth router for interacting with the database."""

    @staticmethod
    def signup(user_in: UserCreate, db: Session) -> UserRead:
        """Creates a new user in the DB.

        Args:
            user_in (UserCreate): Desired user credentials.
            db (Session): DB session for I/O operations.

        Raises:
            HTTPException: 400 if the username is already taken.

        Returns:
            UserRead: Newly created user data.
        """
        existing = db.query(User).filter(User.username == user_in.username).first()
        if existing:
            raise HTTPException(status_code=400, detail="Username already taken")

        user = User(username=user_in.username)
        db.add(user)
        db.commit()
        db.refresh(user)

        return UserRead.model_validate(user)

    @staticmethod
    def login(user_in: UserCreate, db: Session) -> UserRead:
        """Logs in a user based on their credentials.

        Args:
            user_in (UserCreate): User credentials.
            db (Session): DB session for I/O operations.

        Raises:
            HTTPException: 400 if the user is not found.

        Returns:
            UserRead: Authenticated user data.
        """
        user = db.query(User).filter(User.username == user_in.username).first()
        if not user:
            raise HTTPException(status_code=400, detail="Invalid username")

        return UserRead.model_validate(user)

    @staticmethod
    def get_current_user_profile(user: User) -> UserRead:
        """Returns the authenticated user's profile.

        Args:
            user (User): Authenticated user instance.

        Returns:
            UserRead: Authenticated user data.
        """
        return UserRead.model_validate(user)
