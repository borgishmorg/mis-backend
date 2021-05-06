from fastapi import APIRouter
from .actions import (
    get_role,
    get_roles,
    post_role,
    delete_role,
    put_role
)
from .schemas import (
    Role,
    Roles
)


router = APIRouter(
    prefix='/roles',
    tags=['roles']
)
router.add_api_route(
    path='',
    endpoint=get_roles,
    response_model=Roles,
    methods=['GET']
)
router.add_api_route(
    path='/{code}',
    endpoint=get_role,
    response_model=Role,
    methods=['GET']
)
router.add_api_route(
    path='',
    endpoint=post_role,
    response_model=Role,
    methods=['POST']
)
router.add_api_route(
    path='/{code}',
    endpoint=put_role,
    response_model=Role,
    methods=['PUT']
)
router.add_api_route(
    path='/{code}',
    endpoint=delete_role,
    methods=['DELETE']
)
