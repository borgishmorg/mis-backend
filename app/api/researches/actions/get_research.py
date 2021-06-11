from fastapi import Path, Depends
from app.dependencies.token import TokenPayload, token_payload, Permission
from ..controller import ResearchesController
from ..schemas import Research


async def get_research(
    research_id: int = Path(...),
    researches_controller: ResearchesController = Depends(),
    token_payload: TokenPayload = Depends(
        token_payload(permissions=[Permission.RESEARCHES_VIEW])
    )
) -> Research:
    return researches_controller.get_research(
        research_id=research_id
    )
