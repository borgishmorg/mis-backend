from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..controller import AuthController, AuthException
from ..schemas import Tokens


def post_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth: AuthController = Depends()
) -> Tokens:
    try:
        return auth.get_tokens(
            login=form_data.username,
            password=form_data.password
        )
    except AuthException as exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exception)
        )
