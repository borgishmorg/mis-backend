from fastapi import Depends
from app.dependencies import token_payload, Permission, TokenPayload
from ..controller import PatientsController
from ..schemas import Patients


def get_patients(
    patients: PatientsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.USERS_VIEW]))
) -> Patients:
    return patients.get_patients()
