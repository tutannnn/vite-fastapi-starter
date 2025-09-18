from pydantic import BaseModel, constr
from typing import Annotated

class TodoCreate(BaseModel):
    text: str

class TodoRead(BaseModel):
    id: int
    text: Annotated[str, constr(max_length=30)]

    class Config:
        orm_mode = True
