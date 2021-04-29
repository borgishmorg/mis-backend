from fastapi import APIRouter
from .get_status import get_status

router = APIRouter(
    prefix='/api/v1'
)
router.add_api_route(
    path='/status',
    endpoint=get_status,
    tags=['other'],
    methods=['GET']
)
