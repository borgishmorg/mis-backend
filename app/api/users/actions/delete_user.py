from fastapi import Path, Depends, status, HTTPException
from app.dependencies import TokenPayload, token_payload, Permission
from ..controller import UsersController, UserDoesNotExistException
from ..schemas import User


async def delete_user(
    id: int = Path(...),
    token_payload: TokenPayload = Depends(token_payload(
        permissions=[Permission.USERS_ADD]
    )),
    users: UsersController = Depends()
) -> User:
    try:
        return users.delete_user(id)
    except UserDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
