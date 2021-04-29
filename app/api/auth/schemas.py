from pydantic import (
    BaseModel,
    Field
)


class Tokens(BaseModel):
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class Login(BaseModel):
    login: str
    password: str


class Refresh(BaseModel):
    token: str
