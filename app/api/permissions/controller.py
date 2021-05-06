from fastapi.encoders import jsonable_encoder
from app.services import session_scope
from app.models import Permission as PermissionModel
from .schemas import Permissions


class PermissionsController:

    def get_permissions(self) -> Permissions:
        with session_scope() as session:
            permissions = session.query(PermissionModel).all()
            return Permissions(permissions=jsonable_encoder(permissions))
