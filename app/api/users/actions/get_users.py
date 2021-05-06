from fastapi import Depends
from app.dependencies import token_payload, TokenPayload, Permission
from ..controller import UsersController
from ..schemas import Users


async def get_users(
    token_payload: TokenPayload = Depends(token_payload(
        permissions=[Permission.USERS_VIEW]
    )),
    users: UsersController = Depends()
) -> Users:    
    return users.get_users()
