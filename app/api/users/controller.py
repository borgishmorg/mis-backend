from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from app.hash import check_password_hash, generate_password_hash
from app.services import session_scope
from app.models import (
    User as UserModel,
    Role as RoleModel
)
from app.constants import Constants
from .schemas import (
    UserIn, 
    User,
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


class OldPasswordDoesNotSpecifiedException(Exception):

    def __init__(self) -> None:
        super().__init__(Constants.Users.OLD_PASSWORD_DOES_NOT_SPECIFIED_MSG)


class WrongOldPasswordException(Exception):

    def __init__(self) -> None:
        super().__init__(Constants.Users.WRONG_OLD_PASSWORD_MSG)


class NewPasswordDoesNotSpecifiedException(Exception):

    def __init__(self) -> None:
        super().__init__(Constants.Users.NEW_PASSWORD_DOES_NOT_SPECIFIED_MSG)


class UsersController:

    def add_user(
        self,
        user_in: UserIn
    ) -> User:
        'Add new user with specified login, password and role'
        hash = generate_password_hash(user_in.password).hex()
        user = UserModel(
            login=user_in.login, 
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
            except IntegrityError:
                raise UserAlreadyExistsException(user_in.login)
            return User(
                id=user.id,
                login=user.login,
                role=jsonable_encoder(user.role)
            )

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
                if user_in.login is not None:
                    user.login = user_in.login
                
                if (
                    user_in.password is not None
                    # user_in.old_password is not None
                    # or user_in.new_password is not None
                ):
                    # if user_in.old_password is None:
                    #     raise OldPasswordDoesNotSpecifiedException()
                    # if user_in.new_password is None:
                    #     raise NewPasswordDoesNotSpecifiedException()
                    # if not check_password_hash(
                    #     user_in.old_password, 
                    #     user.password_hash
                    # ):
                    #     raise WrongOldPasswordException()
                    user.password_hash = generate_password_hash(user_in.password).hex()

                if user_in.role is not None:
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
            return User(
                id=user.id,
                login=user.login,
                role=jsonable_encoder(user.role)
            )

    def delete_user(
        self,
        id: int
    ):
        'Deletes user with current id'
        with session_scope() as session:
            user = session.get(UserModel, id)
            if user is None:
                raise UserDoesNotExistException(id)
            session.delete(user) # TODO replace with flag
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
