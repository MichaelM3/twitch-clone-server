from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str

class Register(BaseModel):
    username: str
    email: str
    password: str
