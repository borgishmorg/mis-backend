from datetime import datetime, timedelta
import jwt
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload
from app.models import (
    User as UserModel
)
from app.hash import check_password_hash
from app.settings import settings
from app.services.postgres import session_scope
from app.dependencies import TokenPayload
from app.constants import Constants
from .schemas import Tokens


class AuthException(Exception):

    def __init__(self, detail: str) -> None:
        super().__init__(detail)


class WrongUserOrPasswordException(AuthException):

    def __init__(self) -> None:
        super().__init__(Constants.Auth.WRONG_USER_OR_PASSWORD_MSG)


class AuthController:

    def get_tokens(
        self,
        login: str,
        password: str
    ) -> Tokens:
        with session_scope() as session:
            user = (
                session
                .query(UserModel)
                .options(joinedload(UserModel.role))
                .filter(UserModel.login == login)
                .first()
            )

            if (
                user is None 
                or not check_password_hash(
                    password, 
                    user.password_hash
                )
            ):
                raise WrongUserOrPasswordException()
            user = TokenPayload.User(
                **jsonable_encoder(user),
                permissions=[p.code for p in user.role.permissions],
            )
            return Tokens(
                user=user,
                access_token=self.get_access_token(user),
                refresh_token=self.get_refresh_token(user)
            )

    def refresh_tokens(
        self,
        user: TokenPayload.User
    ) -> Tokens:
        # TODO update from db
        return Tokens(
            user=user,
            access_token=self.get_access_token(user),
            refresh_token=self.get_refresh_token(user)
        )

    def get_access_token(
        self,
        user: TokenPayload.User
    ) -> str:
        return jwt.encode(
            payload={
                'user': user.dict(),
                'token_type': 'access',
                'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_ACCESS_TOKEN_LIFETIME)
            },
            key=settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM
        )

    def get_refresh_token(
        self,
        user: TokenPayload.User
    ) -> str:
        return jwt.encode(
            payload={
                'user': user.dict(),
                'token_type': 'refresh',
                'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_REFRESH_TOKEN_LIFETIME)
            },
            key=settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM
        )
