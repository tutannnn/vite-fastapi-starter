"""Defines user authentication services.

NOTE: This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
"""

from fastapi import HTTPException
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from todo.api.v1.schemas.auth import UserCreate, UserRead
from todo.db.models.user import User


class AuthService:
    """Services called by the auth router for interacting with the database."""

    @staticmethod
    async def signup(user_in: UserCreate, db: AsyncSession) -> UserRead:
        """Creates a new user in the DB.

        Args:
            user_in (UserCreate): Desired user credentials.
            db (AsyncSession): DB session for I/O operations.

        Raises:
            HTTPException: 400 if the username is already taken.

        Returns:
            UserRead: Newly created user data.
        """
        logger.info(
            "Signing up user",
            extra={
                "username": user_in.username,
            },
        )

        stmt = select(User).filter(User.username == user_in.username)
        result = await db.execute(stmt)
        existing = result.scalars().first()

        if existing:
            err_msg = "Username already taken"
            logger.error(
                err_msg,
                extra={
                    "username": user_in.username,
                },
            )
            raise HTTPException(status_code=400, detail=err_msg)

        user = User(username=user_in.username)
        db.add(user)
        await db.commit()
        await db.refresh(user)

        logger.info(
            "Signed up user successfully",
            extra={
                "user_id": user.id,
                "username": user.username,
            },
        )

        return UserRead.model_validate(user)

    @staticmethod
    async def login(user_in: UserCreate, db: AsyncSession) -> UserRead:
        """Logs in a user based on their credentials.

        Args:
            user_in (UserCreate): User credentials.
            db (AsyncSession): DB session for I/O operations.

        Raises:
            HTTPException: 400 if the user is not found.

        Returns:
            UserRead: Authenticated user data.
        """
        logger.info(
            "Logging in user",
            extra={
                "username": user_in.username,
            },
        )

        stmt = select(User).filter(User.username == user_in.username)
        result = await db.execute(stmt)
        user = result.scalars().first()

        if not user:
            err_msg = "Invalid username"
            logger.error(
                err_msg,
                extra={
                    "username": user_in.username,
                },
            )
            raise HTTPException(status_code=400, detail=err_msg)

        logger.info(
            "Logged in user successfully",
            extra={
                "user_id": user.id,
                "username": user.username,
            },
        )

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
