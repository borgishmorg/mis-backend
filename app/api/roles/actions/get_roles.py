from fastapi import Depends
from app.dependencies import Permission, token_payload, TokenPayload
from ..controller import RolesController
from ..schemas import Roles


async def get_roles(
    token_payload: TokenPayload = Depends(token_payload(
        permissions=[Permission.ROLES_VIEW]
    )),
    roles: RolesController = Depends()
) -> Roles:
    return roles.get_roles()
