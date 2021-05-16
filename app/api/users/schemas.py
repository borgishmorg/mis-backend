from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class UserBase(BaseModel):
    login: str = Field(max_lenght=255)
    first_name: str = Field(max_length=80)
    surname: str = Field(max_length=80)
    patronymic: Optional[str] = Field(max_length=80)
    birthdate: Optional[date]
    address: Optional[str] = Field(max_length=255)
    phone: Optional[str] = Field(max_length=15)
    email: Optional[str] = Field(max_length=320)
    blocked: bool = False


class UserIn(UserBase):
    password: str
    role: str


class UserInOptional(UserIn):
    password: Optional[str]


class User(UserBase):
    class Role(BaseModel):
        code: str = Field(max_lenght=255)
        name: str = Field(max_lenght=255)

    id: int
    login: str = Field(max_lenght=255)
    role: Optional[Role]


class Users(BaseModel):
    users: list[User]
