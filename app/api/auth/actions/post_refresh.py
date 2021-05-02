from fastapi import Depends
from app.dependencies import token_payload, TokenPayload, TokenType
from ..controller import AuthController
from ..schemas import Tokens


def post_refresh(
    token_payload: TokenPayload = Depends(
        token_payload(token_type=TokenType.REFRESH)
    ),
    auth: AuthController = Depends()
) -> Tokens:
    return auth.refresh_tokens(token_payload.user)
