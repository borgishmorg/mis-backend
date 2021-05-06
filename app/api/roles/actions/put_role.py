from fastapi import Depends, HTTPException, status, Path
from app.dependencies import Permission, token_payload, TokenPayload
from ..controller import (
    RolesController, 
    RoleDoesNotExistException,
    PermissionDoesNotExistException,
    RoleAlredyExistsException
)
from ..schemas import Role, RoleIn


async def put_role(
    role_in: RoleIn,
    code: str = Path(...),
    token_payload: TokenPayload = Depends(token_payload(
        permissions=[Permission.ROLES_EDIT]
    )),
    roles: RolesController = Depends()
) -> Role:
    try:
        return roles.update_role(code, role_in)
    except RoleAlredyExistsException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
    except RoleDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
    except PermissionDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exception)
        )
