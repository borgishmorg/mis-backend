from fastapi import APIRouter
from .get_status import get_status
from .auth import router as auth_router
from .users import router as users_router
from .permissions import router as permissions_router


router = APIRouter(
    prefix='/api/v1'
)
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(permissions_router)
router.add_api_route(
    path='/status',
    endpoint=get_status,
    tags=['other'],
    methods=['GET']
)
