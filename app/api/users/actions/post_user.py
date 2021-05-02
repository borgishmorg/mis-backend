from fastapi import Depends
from ..schemas import UserLogin
from ..controller import UsersController


async def post_user(
    user_login: UserLogin,
    users: UsersController = Depends()
):
    return users.create_user(user_login)
