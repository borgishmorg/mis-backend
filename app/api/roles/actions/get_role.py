from fastapi import Path, Depends, HTTPException, status
from app.dependencies import Permission, token_payload, TokenPayload
from ..controller import RolesController, RoleDoesNotExistException
from ..schemas import Role


async def get_role(
    code: str = Path(...),
    token_payload: TokenPayload = Depends(token_payload(
        permissions=[Permission.ROLES_VIEW]
    )),
    roles: RolesController = Depends()
) -> Role:
    try:
        return roles.get_role(code)
    except RoleDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
