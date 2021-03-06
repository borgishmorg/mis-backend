from fastapi import Path, Depends, status, HTTPException
from app.dependencies import TokenPayload, token_payload, Permission
from ..controller import UsersController, UserDoesNotExistException
from ..schemas import User


async def get_user(
    id: int = Path(...),
    token_payload: TokenPayload = Depends(token_payload(
        check_id=True,
        permissions=[Permission.USERS_VIEW]
    )),
    users: UsersController = Depends()
) -> User:
    try:
        return users.get_user(id)
    except UserDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
