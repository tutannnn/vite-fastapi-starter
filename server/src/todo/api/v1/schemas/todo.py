from pydantic import BaseModel, ConfigDict


class TodoCreate(BaseModel):
    text: str


class TodoRead(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)
