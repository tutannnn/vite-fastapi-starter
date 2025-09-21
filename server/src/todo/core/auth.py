"""Utilities for user authentication and authorization.

TODO: Note that the implementation below is meant solely for dev and is meant to be replaced by production-ready
solutions like Auth0/RBAC/JWTs/OAuth/etc.
"""

from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session

from todo.db.models.user import User
from todo.db.session import get_db


def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    """Returns the current user from the database based on a mock header of the form `Authorization: Bearer <USER_ID>`.

    TODO: Replace this logic with your production-ready solution like Auth0, etc.

    Args:
        request (Request): HTTP request containing the mock AuthZ header.
        db (Session, optional): DB session for I/O. Defaults to Depends(get_db).

    Raises:
        HTTPException: 401 if the AuthZ header is missing or malformed.
        HTTPException: 404 if the user ID does not exist in the DB.

    Returns:
        User: The relevant user instance from the DB.
    """
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    user_id = auth.replace("Bearer ", "").strip()
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
