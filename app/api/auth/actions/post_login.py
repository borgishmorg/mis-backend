from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import Tokens


def post_login(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Tokens:
    if form_data.username != 'user' or form_data.password != 'user':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid username or password'
        )
    return {
        'access_token': 'access',
        'refresh_token': 'refresh'
    }
