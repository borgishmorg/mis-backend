from pydantic import BaseModel


class Permission(BaseModel):
    code: str
    name: str


class Permissions(BaseModel):
    permissions: list[Permission]
