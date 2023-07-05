from pydantic import BaseModel
from datetime import datetime

from app.schemas.auth import UserBase


class PostBase(BaseModel):
    title: str
    text: str
    date: datetime

    class Config:
        orm_mode = True


class GetPost(PostBase):
    author: UserBase
    likes: int
    dislikes: int

    class Config:
        orm_mode = True

    
class EditPost(PostBase):
    title: str | None = None
    text: str | None = None
    date: datetime | None = None