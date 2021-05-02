from fastapi import APIRouter
from .actions import (
    post_user
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
