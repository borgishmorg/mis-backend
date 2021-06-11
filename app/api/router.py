from fastapi import APIRouter
from .get_status import get_status
from .auth import router as auth_router
from .users import router as users_router
from .permissions import router as permissions_router
from .roles import router as roles_router
from .patients import router as patients_router
from .examinations import router as examinations_router
from .researches import router as researches_router


router = APIRouter(
    prefix='/api'
)
router.include_router(auth_router, prefix='/v1')
router.include_router(users_router, prefix='/v1')
router.include_router(roles_router, prefix='/v1')
router.include_router(permissions_router, prefix='/v1')
router.include_router(patients_router, prefix='/v1')
router.include_router(examinations_router, prefix='/v1')
router.include_router(researches_router, prefix='/v1')
router.add_api_route(
    path='/status',
    endpoint=get_status,
    tags=['other'],
    methods=['GET']
)
