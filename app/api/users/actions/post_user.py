from fastapi import Depends, HTTPException, status
from app.dependencies import token_payload, TokenPayload, Permission
from ..schemas import UserIn
from ..controller import (
    UsersController, 
    UserAlreadyExistsException,
    RoleDoesNotExistException
)


async def post_user(
    user_in: UserIn,
    token_payload: TokenPayload = Depends(token_payload(
        permissions=[Permission.USERS_EDIT]
    )),
    users: UsersController = Depends()
):
    try:
        return users.add_user(user_in)
    except UserAlreadyExistsException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
    except RoleDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exception)
        )
