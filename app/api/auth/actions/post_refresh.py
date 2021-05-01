from fastapi.param_functions import Depends
from ..schemas import Tokens
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")


def post_refresh(
    token: str = Depends(oauth2_scheme)
) -> Tokens:
    return {
        'access_token': 'access',
        'refresh_token': 'refresh'
    }
