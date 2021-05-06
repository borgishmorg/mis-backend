from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError
from app.constants import Constants
from app.services import session_scope
from app.models import (
    Role as RoleModel,
    Permission as PermissionModel
)
from .schemas import Role, RoleIn, Roles


class RoleAlreadyExistsException(Exception):

    def __init__(self, code: str) -> None:
        super().__init__(Constants.Roles.ROLE_ALREADY_EXISTS_MSG)


class RoleDoesNotExistException(Exception):

    def __init__(self, code: str) -> None:
        super().__init__(Constants.Roles.ROLE_DOES_NOT_EXIST_MSG.format(code=code))


class RoleIsNotEmptyException(Exception):

    def __init__(self, code: str) -> None:
        super().__init__(Constants.Roles.ROLE_IS_NOT_EMPTY_MSG.format(code=code))


class PermissionDoesNotExistException(Exception):

    def __init__(self, code: str) -> None:
        super().__init__(Constants.Roles.PERMISSION_DOES_NOT_EXIST_MSG.format(code=code))


class RolesController:

    def add_role(
        self,
        role_in: RoleIn
    ) -> Role:
        with session_scope() as session:
            role = RoleModel(
                code=role_in.code,
                name=role_in.name
            )

            for permission_code in role_in.permissions:
                permission = (
                    session
                    .query(PermissionModel)
                    .filter_by(code=permission_code)
                    .first()
                )
                if permission is None:
                    raise PermissionDoesNotExistException(code=permission_code)
                role.permissions.append(permission)

            try:
                session.add(role)
                session.flush()
            except IntegrityError:
                raise RoleAlreadyExistsException(role_in.code)

            return Role(
                code=role.code,
                name=role.name,
                permissions=jsonable_encoder(role.permissions)
            )

    def update_role(
        self,
        code: str,
        role_in: RoleIn
    ) -> Role:
        with session_scope() as session:
            role = (
                session
                .query(RoleModel)
                .filter_by(code=code)
                .first()
            )
            if role is None:
                raise RoleDoesNotExistException(code)

            try:
                role.code = role_in.code
                role.name = role_in.name
                role.permissions.clear()
                for permission_code in role_in.permissions:
                    permission = (
                        session
                        .query(PermissionModel)
                        .filter_by(code=permission_code)
                        .first()
                    )
                    if permission is None:
                        raise PermissionDoesNotExistException(code=permission_code)
                    role.permissions.append(permission)
                session.flush()
            except IntegrityError:
                raise RoleAlreadyExistsException(role_in.code)

            return Role(
                code=role.code,
                name=role.name,
                permissions=jsonable_encoder(role.permissions)
            )

    def delete_role(
        self,
        code: str
    ):
        with session_scope() as session:
            role = (
                session
                .query(RoleModel)
                .options(joinedload(RoleModel.permissions))
                .filter_by(code=code)
                .first()
            )
            if role is None:
                raise RoleDoesNotExistException(code)
            try:
                session.delete(role)
                session.flush()
            except IntegrityError:
                raise RoleIsNotEmptyException(code)

    def get_role(
        self,
        code: str
    ) -> Role:
        with session_scope() as session:
            role = (
                session
                .query(RoleModel)
                .options(joinedload(RoleModel.permissions))
                .filter_by(code=code)
                .first()
            )
            if role is None:
                raise RoleDoesNotExistException(code)
            return Role(**jsonable_encoder(role))

    def get_roles(
        self
    ) -> Roles:
        with session_scope() as session:
            roles = (
                session
                .query(RoleModel)
                .options(joinedload(RoleModel.permissions))
                .all()
            )
            return Roles(roles=jsonable_encoder(roles))
