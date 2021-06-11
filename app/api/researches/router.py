from fastapi import APIRouter
from .actions import (
    get_researches,
    get_research,
    get_research_file,
    post_research,
    delete_research
)


router = APIRouter(
    prefix='/researches',
    tags=['researches']
)
router.add_api_route(
    path='',
    endpoint=get_researches,
    methods=['GET']
)
router.add_api_route(
    path='/{research_id}',
    endpoint=get_research,
    methods=['GET']
)
router.add_api_route(
    path='/{research_id}/file',
    endpoint=get_research_file,
    methods=['GET']
)
router.add_api_route(
    path='',
    endpoint=post_research,
    methods=['POST']
)
router.add_api_route(
    path='/{research_id}',
    endpoint=delete_research,
    methods=['DELETE']
)
