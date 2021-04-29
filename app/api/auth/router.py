from fastapi import APIRouter
from .actions import (
    post_login,
    post_refresh,
)
from .schemas import (
    Tokens,
)


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)
router.add_api_route(
    path='/login',
    endpoint=post_login,
    response_model=Tokens,
    methods=['POST']
)
router.add_api_route(
    path='/refresh',
    endpoint=post_refresh,
    response_model=Tokens,
    methods=['POST']
)
