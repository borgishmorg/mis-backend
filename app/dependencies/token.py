import enum
from typing import Callable
import jwt
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.settings import settings


class TokenType(enum.Enum):
    ACCESS: str = 'access'
    REFRESH: str = 'refresh'


class TokenPayload(BaseModel):
    class User(BaseModel):
        id: int
        login: str

    user: User
    token_type: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")


class TokenException(HTTPException):

    def __init__(self, detail: str) -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail=detail)


def token_payload(
    token_type: TokenType = TokenType.ACCESS
) -> Callable[..., TokenPayload]:
    def dependency(
        token: str = Depends(oauth2_scheme)
    ) -> TokenPayload:
        try:
            payload = TokenPayload(**jwt.decode(
                jwt=token,
                key=settings.JWT_SECRET,
                verify=True,
                algorithms=settings.JWT_ALGORITHM
            ))
        except jwt.InvalidSignatureError:
            import traceback
            traceback.print_exc()
            raise TokenException('Invalid token signature')
        except jwt.ExpiredSignatureError:
            raise TokenException('Token had been expired')
        except jwt.InvalidTokenError:
            raise TokenException('Invalid token')

        if payload.token_type != token_type.value:
            raise TokenException('Wrong token type')
        return payload
    return dependency
