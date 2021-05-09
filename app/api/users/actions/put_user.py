from fastapi import Depends, HTTPException, status, Path
from app.dependencies import token_payload, TokenPayload, Permission
from ..schemas import UserInOptional
from ..controller import (
    UsersController, 
    UserDoesNotExistException,
    UserAlreadyExistsException,
    RoleDoesNotExistException,
    OldPasswordDoesNotSpecifiedException,
    NewPasswordDoesNotSpecifiedException,
    WrongOldPasswordException
)


async def put_user(
    user_in: UserInOptional,
    id: int = Path(...),
    token_payload: TokenPayload = Depends(token_payload(
        # check_id=True,
        permissions=[Permission.USERS_EDIT]
    )),
    users: UsersController = Depends()
):
    try:
        return users.update_user(id, user_in)
    except UserDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
    except UserAlreadyExistsException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
    except (
        RoleDoesNotExistException,
        OldPasswordDoesNotSpecifiedException,
        NewPasswordDoesNotSpecifiedException,
        WrongOldPasswordException
    ) as exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exception)
        )
