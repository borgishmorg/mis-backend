from datetime import datetime, timedelta
import jwt
from fastapi.encoders import jsonable_encoder
from app.models import (
    User as UserModel
)
from app.hash import check_password_hash
from app.settings import settings
from app.services.postgres import session_scope
from app.dependencies import TokenPayload
from .schemas import Tokens


class AuthException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


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
                .filter(UserModel.login == login)
                .first()
            )

            if (
                user is None 
                or not check_password_hash(
                    password, 
                    user.password_hash)
            ):
                raise AuthException('Wrong user/password')
            user = TokenPayload.User(**jsonable_encoder(user))

        return Tokens(
            access_token=self.get_access_token(user),
            refresh_token=self.get_refresh_token(user)
        )

    def refresh_tokens(
        self,
        user: TokenPayload.User
    ) -> Tokens:
        return Tokens(
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
