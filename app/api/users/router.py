from fastapi import APIRouter

from .schemas import (
    User,
)
from .actions import (
    post_user,
    get_user,
)


router = APIRouter(
    prefix='/users',
    tags=['users']
)
router.add_api_route(
    path='',
    endpoint=post_user,
    # response_model=,
    methods=['POST']
)
router.add_api_route(
    path='/{id:int}',
    endpoint=get_user,
    response_model=User,
    methods=['GET']
)
