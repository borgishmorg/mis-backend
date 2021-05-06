from fastapi import Depends
from app.dependencies import token_payload, Permission, TokenPayload
from ..controller import PermissionsController
from ..schemas import Permissions


async def get_permissions(
    token_payload: TokenPayload = Depends(token_payload(
        permissions=[Permission.PERMISSIONS_VIEW]
    )),
    permissions: PermissionsController = Depends()
) -> Permissions:
    return permissions.get_permissions()
