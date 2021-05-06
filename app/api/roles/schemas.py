from pydantic import BaseModel


class Permission(BaseModel):
    code: str
    name: str


class Role(BaseModel):
    code: str
    name: str
    permissions: list[Permission]


class Roles(BaseModel):
    roles: list[Role]


class RoleIn(BaseModel):
    code: str
    name: str
    permissions: list[str]
