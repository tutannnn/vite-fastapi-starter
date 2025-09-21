"""Pydantic schemas for todo-related operations."""

from pydantic import BaseModel, ConfigDict


class TodoCreate(BaseModel):
    """Schema for creating a new todo item."""

    text: str


class TodoRead(BaseModel):
    """Schema for reading a todo item from the database."""

    id: int
    text: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)
