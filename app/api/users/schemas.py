from pydantic import BaseModel


class Credentials(BaseModel):
    login: str
    password: str


class User(BaseModel):
    id: int
    login: str
