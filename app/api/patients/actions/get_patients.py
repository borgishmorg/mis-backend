from typing import Optional
from fastapi import Depends, Query
from app.dependencies import token_payload, Permission, TokenPayload
from ..controller import PatientsController
from ..schemas import Patients


def get_patients(
    offset: int = Query(0, ge=0),
    limit: int = Query(50, gt=0),
    q: Optional[str] = None,
    patients: PatientsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.PATIENTS_VIEW]))
) -> Patients:
    if q is None:
        return patients.get_patients(
            offset=offset, 
            limit=limit
        )
    else:
        return patients.search_patients(
            q=q,
            offset=offset, 
            limit=limit
        )
