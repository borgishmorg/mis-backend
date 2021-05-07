from pydantic import BaseModel
from app.dependencies import TokenPayload


class Tokens(BaseModel):
    user: TokenPayload.User
    access_token: str
    refresh_token: str
    token_type: str = 'bearer'
