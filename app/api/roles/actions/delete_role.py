from fastapi import Path, Depends, HTTPException, status
from app.dependencies import Permission, token_payload, TokenPayload
from ..controller import (
    RolesController, 
    RoleDoesNotExistException,
    RoleIsNotEmptyException
)
from ..schemas import Role


async def delete_role(
    code: str = Path(...),
    token_payload: TokenPayload = Depends(token_payload(
        permissions=[Permission.ROLES_EDIT]
    )),
    roles: RolesController = Depends()
) -> Role:
    try:
        roles.delete_role(code)
    except RoleDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
    except RoleIsNotEmptyException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
