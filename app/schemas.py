from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class ChannelBase(BaseModel):
    description: str

class UserCreate(UserBase):
    plain_password: str

class User(UserBase):
    id: int
    avatar: Optional[str] = None
    is_creator: bool
    following: List[ChannelBase] = []

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class ChannelCreate(ChannelBase):
    pass   

class Creator(User):
    channel: ChannelBase

class Channel(ChannelBase):
    id: int
    is_live: bool
    owner: Creator 
    created_at: datetime
    follows: List[UserBase] = []

