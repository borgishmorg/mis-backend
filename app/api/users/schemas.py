from typing import Optional
from pydantic import BaseModel


class Credentials(BaseModel):
    login: str
    password: str


class User(BaseModel):
    class Role(BaseModel):
        code: str
        name: str

    id: int
    login: str
    role: Optional[Role]


class Users(BaseModel):
    users: list[User]
