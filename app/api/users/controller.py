from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from app.hash import generate_password_hash
from app.services import session_scope
from app.models import (
    User as UserModel,
)
from app.constants import Constants
from .schemas import (
    Credentials, 
    User,
    Users,
)


class UserException(Exception):

    def __init__(self, details: str) -> None:
        super().__init__(details)


class UserAlreadyExistsException(UserException):

    def __init__(self, login: str) -> None:
        super().__init__(Constants.Users.USER_ALREDY_EXISTS_MSG.format(login=login))


class UserDoNotExistsException(UserException):

    def __init__(self, id: int) -> None:
        super().__init__(Constants.Users.USER_DO_NOT_EXISTS_MSG.format(id=id))


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

    def get_user(
        self,
        id: int
    ) -> User:
        'Returns user with current id'
        with session_scope() as session:
            user = session.get(UserModel, id, [joinedload(UserModel.role)])
            if user is None:
                raise UserDoNotExistsException(id)
            return User(**jsonable_encoder(user))

    def get_users(
        self
    ) -> Users:
        'Returns all users'
        with session_scope() as session:
            users = (
                session
                .query(UserModel)
                .options(joinedload(UserModel.role))
                .all()
            )
            return Users(users=jsonable_encoder(users))
