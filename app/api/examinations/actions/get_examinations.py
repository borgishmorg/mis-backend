from typing import Optional
from fastapi import Depends, Query
from app.dependencies import token_payload, Permission, TokenPayload
from ..controller import ExaminationsController
from ..schemas import Examinations


def get_examinations(
    offset: int = Query(0, ge=0),
    limit: int = Query(50, gt=0),
    patient_id: Optional[int] = None,
    examinations: ExaminationsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.EXAMINATIONS_VIEW]))
) -> Examinations:
    if patient_id is None:
        return examinations.get_examinations(
            offset=offset, 
            limit=limit
        )
    else:
        return examinations.search_examinations(
            patient_id=patient_id,
            offset=offset, 
            limit=limit
        )
