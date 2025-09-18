from typing import Annotated

from pydantic import BaseModel, constr


class TodoCreate(BaseModel):
    text: str


class TodoRead(BaseModel):
    id: int
    text: Annotated[str, constr(max_length=30)]

    class Config:
        orm_mode = True
