from fastapi import APIRouter

from .schemas import (
    User,
    Users,
)
from .actions import (
    post_user,
    get_user,
    get_users,
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
router.add_api_route(
    path='',
    endpoint=get_users,
    response_model=Users,
    methods=['GET']
)
