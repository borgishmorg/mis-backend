from fastapi import APIRouter
from .actions import (
    get_examination,
    get_examinations,
    post_examination,
    put_examination,
    delete_examination
)
from .schemas import (
    Examinations, Examination
)


router = APIRouter(
    prefix='/examinations',
    tags=['examinations']
)
router.add_api_route(
    path='',
    endpoint=get_examinations,
    response_model=Examinations,
    methods=['GET']
)
router.add_api_route(
    path='',
    endpoint=post_examination,
    response_model=Examination,
    methods=['POST']
)
router.add_api_route(
    path='/{id}',
    endpoint=get_examination,
    response_model=Examination,
    methods=['GET']
)
router.add_api_route(
    path='/{id}',
    endpoint=put_examination,
    response_model=Examination,
    methods=['PUT']
)
router.add_api_route(
    path='/{id}',
    endpoint=delete_examination,
    methods=['DELETE']
)
