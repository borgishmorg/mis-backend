from pydantic import BaseModel


class UserLogin(BaseModel):
    login: str
    password: str


class User(BaseModel):
    id: int
    login: str
