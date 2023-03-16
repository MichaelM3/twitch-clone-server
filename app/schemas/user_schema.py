from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    avatar: Optional[str] = None
    is_creator: bool

    class Config:
        orm_mode = True

