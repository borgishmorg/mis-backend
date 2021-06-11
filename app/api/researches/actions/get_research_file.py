from fastapi import Path, Depends
from fastapi.responses import FileResponse
from app.dependencies.token import TokenPayload, token_payload, Permission
from ..controller import ResearchesController


async def get_research_file(
    research_id: int = Path(...),
    researches_controller: ResearchesController = Depends(),
    token_payload: TokenPayload = Depends(
        token_payload(permissions=[Permission.RESEARCHES_VIEW])
    )
) -> FileResponse:
    return researches_controller.get_research_file(
        research_id=research_id
    )
