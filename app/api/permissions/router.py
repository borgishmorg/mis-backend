from fastapi import APIRouter
from .actions import (
    get_permissions
)
from .schemas import (
    Permissions
)


router = APIRouter(
    prefix='/permissions',
    tags=['permissions']
)
router.add_api_route(
    path='',
    endpoint=get_permissions,
    response_model=Permissions,
    methods=['GET']
)
