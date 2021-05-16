from fastapi import Depends, status, HTTPException
from app.dependencies import token_payload, TokenPayload, TokenType
from ..controller import AuthController, AuthException
from ..schemas import Tokens


def post_refresh(
    token_payload: TokenPayload = Depends(
        token_payload(token_type=TokenType.REFRESH)
    ),
    auth: AuthController = Depends()
) -> Tokens:
    try:
        return auth.refresh_tokens(token_payload.user)
    except AuthException as exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exception)
        )
