from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from app.hash import generate_password_hash
from app.services import session_scope
from app.models import (
    User as UserModel,
    Role as RoleModel
)
from app.constants import Constants
from .schemas import (
    User,
    UserIn, 
    UserInOptional,
    Users,
)


class UserAlreadyExistsException(Exception):

    def __init__(self, login: str) -> None:
        super().__init__(Constants.Users.USER_ALREADY_EXISTS_MSG.format(login=login))


class UserDoesNotExistException(Exception):

    def __init__(self, id: int) -> None:
        super().__init__(Constants.Users.USER_DO_NOT_EXISTS_MSG.format(id=id))


class RoleDoesNotExistException(Exception):

    def __init__(self, code: str) -> None:
        super().__init__(Constants.Users.ROLE_DOES_NOT_EXIST_MSG.format(code=code))


class UsersController:

    def add_user(
        self,
        user_in: UserIn
    ) -> User:
        'Add new user with specified login, password and role'
        hash = generate_password_hash(user_in.password).hex()
        user = UserModel(
            **user_in.dict(exclude={'role', 'password'}),
            password_hash=hash
        )
        with session_scope() as session:
            role = (
                session
                .query(RoleModel)
                .filter_by(code=user_in.role)
                .first()
            )
            if role is None:
                raise RoleDoesNotExistException(user_in.role)
            user.role = role
            try:
                session.add(user)
                session.flush()
                user_id = user.id 
            except IntegrityError:
                raise UserAlreadyExistsException(user_in.login)
        return self.get_user(user_id)

    def update_user(
        self,
        id: int,
        user_in: UserInOptional
    ) -> User:
        'Update user with current id with specified login, password and role'
        with session_scope() as session:
            user: UserModel = session.get(UserModel, id)
            if user is None:
                raise UserDoesNotExistException(id)

            try:
                user.login = user_in.login
                user.first_name = user_in.first_name
                user.surname = user_in.surname
                user.patronymic = user_in.patronymic
                user.birthdate = user_in.birthdate
                user.address = user_in.address
                user.phone = user_in.phone
                user.email = user_in.email
                user.blocked = user_in.blocked

                if user_in.password is not None:
                    user.password_hash = generate_password_hash(user_in.password).hex()

                role = (
                    session
                    .query(RoleModel)
                    .filter_by(code=user_in.role)
                    .first()
                )
                if role is None:
                    raise RoleDoesNotExistException(user_in.role)
                user.role = role

                session.flush()
            except IntegrityError:
                raise UserAlreadyExistsException(user_in.login)
            return self.get_user(user.id)

    def delete_user(
        self,
        id: int
    ):
        'Deletes user with current id'
        with session_scope() as session:
            user = session.get(UserModel, id)
            if user is None:
                raise UserDoesNotExistException(id)
            session.delete(user)
            session.flush()

    def get_user(
        self,
        id: int
    ) -> User:
        'Returns user with current id'
        with session_scope() as session:
            user = session.get(UserModel, id, [joinedload(UserModel.role)])
            if user is None:
                raise UserDoesNotExistException(id)
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
                .order_by(UserModel.id)
                .all()
            )
            return Users(users=jsonable_encoder(users))
