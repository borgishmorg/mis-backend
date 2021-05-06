from fastapi import APIRouter
from .schemas import (
    User,
    Users,
)
from .actions import (
    post_user,
    get_user,
    get_users,
    put_user,
    delete_user
)


router = APIRouter(
    prefix='/users',
    tags=['users']
)
router.add_api_route(
    path='',
    endpoint=get_users,
    response_model=Users,
    methods=['GET']
)
router.add_api_route(
    path='',
    endpoint=post_user,
    response_model=User,
    methods=['POST']
)
router.add_api_route(
    path='/{id:int}',
    endpoint=get_user,
    response_model=User,
    methods=['GET']
)
router.add_api_route(
    path='/{id:int}',
    endpoint=put_user,
    response_model=User,
    methods=['PUT']
)
router.add_api_route(
    path='/{id:int}',
    endpoint=delete_user,
    methods=['DELETE']
)
