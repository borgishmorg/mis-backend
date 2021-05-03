from fastapi import Path, Depends, status, HTTPException
from ..controller import UsersController, UserDoNotExistsException
from ..schemas import User


async def get_user(
    id: int = Path(...),
    users: UsersController = Depends()
) -> User:
    try:
        return users.get_user(id)
    except UserDoNotExistsException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
