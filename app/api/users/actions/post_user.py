from fastapi import Depends, HTTPException, status
from ..schemas import Credentials
from ..controller import UsersController, UserException


async def post_user(
    credentials: Credentials,
    users: UsersController = Depends()
):
    try:
        return users.create_user(credentials)
    except UserException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
