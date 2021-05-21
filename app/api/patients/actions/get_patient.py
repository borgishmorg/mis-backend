from fastapi import Depends, Path, HTTPException, status
from app.dependencies import token_payload, TokenPayload, Permission
from ..controller import PatientsController, PatientDoesNotExistException
from ..schemas import Patient


def get_patient(
    id: int = Path(...),
    patients: PatientsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.USERS_VIEW]))
) -> Patient:
    try:
        return patients.get_patient(id)
    except PatientDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
