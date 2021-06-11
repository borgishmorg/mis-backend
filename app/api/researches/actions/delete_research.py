from fastapi import Path, Depends
from app.dependencies.token import TokenPayload, token_payload, Permission
from ..controller import ResearchesController
from ..schemas import Research


async def delete_research(
    research_id: int = Path(...),
    researches_controller: ResearchesController = Depends(),
    token_payload: TokenPayload = Depends(
        token_payload(permissions=[Permission.RESEARCHES_EDIT])
    )
) -> Research:
    return researches_controller.delete_research(
        research_id=research_id
    )
