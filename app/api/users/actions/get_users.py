from fastapi import Depends
from ..controller import UsersController
from ..schemas import Users


async def get_users(
    users: UsersController = Depends()
) -> Users:    
    return users.get_users()
