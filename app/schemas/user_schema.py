from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(BaseModel):
    avatar: str | None = None
    is_creator: bool | None = None

class User(UserBase):
    id: int
    avatar: str | None = None
    is_creator: bool

    class Config:
        orm_mode = True

