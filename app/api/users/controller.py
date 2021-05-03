from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from app.hash import generate_password_hash
from app.services import session_scope
from app.models import (
    User as UserModel
)
from app.constants import Constants
from .schemas import Credentials, User


class UserException(Exception):

    def __init__(self, details: str) -> None:
        super().__init__(details)


class UserAlreadyExistsException(UserException):

    def __init__(self, login: str) -> None:
        super().__init__(Constants.Users.USER_ALREDY_EXISTS_MSG.format(login=login))


class UsersController:

    def create_user(
        self,
        credentials: Credentials
    ) -> User:
        'Creates new user with specified login and password'
        hash = generate_password_hash(credentials.password).hex()
        user = UserModel(
            login=credentials.login, 
            password_hash=hash
        )
        try:
            with session_scope() as session:
                session.add(user)
                session.flush()
                return User(**jsonable_encoder(user))
        except IntegrityError:
            raise UserAlreadyExistsException(credentials.login)
