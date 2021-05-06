from typing import Optional
from pydantic import BaseModel


class UserIn(BaseModel):
    login: str
    password: str
    role: str


class UserInOptional(BaseModel):
    login: Optional[str]
    old_password: Optional[str]
    new_password: Optional[str]
    role: Optional[str]


class User(BaseModel):
    class Role(BaseModel):
        code: str
        name: str

    id: int
    login: str
    role: Optional[Role]


class Users(BaseModel):
    users: list[User]
