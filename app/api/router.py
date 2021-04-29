from fastapi import APIRouter
from .get_status import get_status
from .auth import router as auth_router

router = APIRouter(
    prefix='/api/v1'
)
router.include_router(auth_router)
router.add_api_route(
    path='/status',
    endpoint=get_status,
    tags=['other'],
    methods=['GET']
)
