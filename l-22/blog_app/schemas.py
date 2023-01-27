from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class CalcInput(BaseModel):
    a: int
    b: int


class UserIn(BaseModel):
    username: str


class UserBase(UserIn):
    id: int
    crated_at: datetime = Field(default_factory=datetime.now)


class UserOut(UserBase):
    class Config:
        orm_mode = True
