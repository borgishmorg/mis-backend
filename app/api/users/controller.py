from fastapi.encoders import jsonable_encoder
from app.hash import generate_password_hash
from app.services import session_scope
from app.models import (
    User as UserModel
)
from .schemas import UserLogin, User


class UserException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UsersController:

    def is_user_exists(
        self,
        login: str
    ) -> bool:
        'Checks is user with current login exists'
        with session_scope() as session:
            return (
                session
                .query(UserModel)
                .filter(UserModel.login == login)
                .count()
            ) > 0

    def create_user(
        self,
        user_login: UserLogin
    ) -> User:
        'Creates new user with specified login and password'
        if self.is_user_exists(user_login.login):
            raise UserException(f'User with login "{user_login.login}" alredy exists')

        hash = generate_password_hash(user_login.password).hex()
        user = UserModel(
            login=user_login.login, 
            password_hash=hash
        )

        with session_scope() as session:
            session.add(user)
            session.flush()
            return User(**jsonable_encoder(user))
