from fastapi import UploadFile, Form, File, Depends
from app.dependencies.token import TokenPayload, token_payload, Permission
from ..controller import ResearchesController
from ..schemas import Research


async def post_research(
    research_file: UploadFile = File(...),
    patient_id: int = Form(...),
    research_name: str = Form(..., max_length=100),
    researches_controller: ResearchesController = Depends(),
    token_payload: TokenPayload = Depends(
        token_payload(permissions=[Permission.RESEARCHES_EDIT])
    )
) -> Research:
    return researches_controller.add_research(
        research_file=research_file,
        user_id=token_payload.user.id,
        patient_id=patient_id,
        research_name=research_name
    )
