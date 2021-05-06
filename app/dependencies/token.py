import enum
from typing import Callable, Optional
import jwt
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status, Path
from fastapi.security import OAuth2PasswordBearer
from app.settings import settings
from app.constants import Constants


class TokenType(enum.Enum):
    ACCESS: str = 'access'
    REFRESH: str = 'refresh'


class Permission(str, enum.Enum):
    PERMISSIONS_VIEW = 'permissions:view'
    ROLES_ADD = 'roles:add'
    ROLES_EDIT = 'roles:edit'
    ROLES_VIEW = 'roles:view'
    USERS_ADD = 'users:add'
    USERS_EDIT = 'users:edit'
    USERS_VIEW = 'users:view'


class TokenPayload(BaseModel):
    class User(BaseModel):
        id: int
        login: str
        permissions: list[Permission]

    user: User
    token_type: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=Constants.Token.LOGIN_URL)


class TokenException(HTTPException):

    def __init__(self, detail: str) -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail=detail)


class ForbiddenException(HTTPException):

    def __init__(self, detail: str) -> None:
        super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)


def token_payload(
    token_type: TokenType = TokenType.ACCESS,
    check_id: bool = False, # skip permissions check if request id equal to current user id
    permissions: Optional[list[Permission]] = None # one of them is required
) -> Callable[..., TokenPayload]:
    def dependency(
        id: Optional[int] = Path(None) if check_id else Depends(lambda: None),
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
            raise TokenException(Constants.Token.INVALID_SIGNATURE_MSG)
        except jwt.ExpiredSignatureError:
            raise TokenException(Constants.Token.EXPIRED_SIGNATURE_MSG)
        except jwt.InvalidTokenError:
            raise TokenException(Constants.Token.INVALID_TOKEN_MSG)

        # Token type check
        if payload.token_type != token_type.value:
            raise TokenException(Constants.Token.WRONG_TOKEN_TYPE_MSG)

        # Permission check
        if (
            permissions is not None 
            and not (
                check_id is not None
                and payload.user.id == id
            )
        ):
            for permission in permissions:
                if permission in payload.user.permissions:
                    break
            else:
                raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
        return payload
    return dependency
