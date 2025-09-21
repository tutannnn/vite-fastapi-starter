"""Pydantic schemas for user authentication-related operations.

NOTE: This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
"""

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    """Schema for creating a new user the database."""

    username: str


class UserRead(BaseModel):
    """Schema for getting a user from the DB."""

    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)
