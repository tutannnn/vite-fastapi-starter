"""Utilities for user authentication and authorization.

NOTE: This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
"""

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from todo.db.models.user import User
from todo.db.session import get_db

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)
) -> User:
    """Returns the current user from the database based on a mock header of the form `Authorization: Bearer <USER_ID>`.

    TODO: Replace this logic with your production-ready solution like Auth0, etc.

    Args:
        credentials (Request): HTTP AuthN credentials.
        db (Session, optional): DB session for I/O. Defaults to Depends(get_db).

    Returns:
        User: The relevant user instance from the DB.
    """
    user_id = int(credentials.credentials)
    user = db.query(User).filter_by(id=user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
