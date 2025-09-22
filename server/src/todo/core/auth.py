"""Utilities for user authentication and authorization.

NOTE: This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
"""

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from todo.db.models.user import User
from todo.db.session import get_db

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security), db: AsyncSession = Depends(get_db)
) -> User:
    """Returns the current user from the database based on a mock header of the form `Authorization: Bearer <USER_ID>`.

    TODO: Replace this logic with your production-ready solution like Auth0, etc.

    Args:
        credentials (Request): HTTP AuthN credentials.
        db (AsyncSession, optional): DB session for I/O. Defaults to Depends(get_db).

    Returns:
        User: The relevant user instance from the DB.
    """
    user_id = int(credentials.credentials)

    logger.info(
        "Getting current user",
        extra={
            "user_id": user_id,
        },
    )

    stmt = select(User).filter_by(id=user_id)
    result = await db.execute(stmt)
    user = result.scalars().first()

    if not user:
        err_msg = "User not found"
        logger.info(
            err_msg,
            extra={
                "user_id": user_id,
            },
        )
        raise HTTPException(status_code=404, detail=err_msg)

    logger.info(
        "Got current user successfully",
        extra={
            "user_id": user.id,
            "username": user.username,
        },
    )

    return user
