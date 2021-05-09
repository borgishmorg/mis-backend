from fastapi import Depends, HTTPException, status
from app.dependencies import Permission, token_payload, TokenPayload
from ..controller import (
    RolesController, 
    RoleAlreadyExistsException,
    PermissionDoesNotExistException
)
from ..schemas import Role, RoleIn


async def post_role(
    role_in: RoleIn,
    token_payload: TokenPayload = Depends(token_payload(
        permissions=[Permission.ROLES_EDIT]
    )),
    roles: RolesController = Depends()
) -> Role:
    try:
        return roles.add_role(role_in)
    except RoleAlreadyExistsException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
    except PermissionDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exception)
        )
