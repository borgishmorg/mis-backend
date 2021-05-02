from fastapi import Depends, HTTPException, status
from ..schemas import UserLogin
from ..controller import UsersController, UserException


async def post_user(
    user_login: UserLogin,
    users: UsersController = Depends()
):
    try:
        return users.create_user(user_login)
    except UserException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
