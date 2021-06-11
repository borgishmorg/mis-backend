from fastapi import Path, Depends
from fastapi.param_functions import Query
from app.dependencies.token import TokenPayload, token_payload, Permission
from ..controller import ResearchesController
from ..schemas import Researches


async def get_researches(
    patient_id: int = Query(...),
    offset: int = Query(0),
    limit: int = Query(50),
    researches_controller: ResearchesController = Depends(),
    token_payload: TokenPayload = Depends(
        token_payload(permissions=[Permission.RESEARCHES_VIEW])
    )
) -> Researches:
    return researches_controller.get_researches(
        patient_id=patient_id,
        offset=offset,
        limit=limit
    )
