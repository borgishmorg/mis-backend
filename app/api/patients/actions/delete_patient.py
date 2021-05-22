from fastapi import Depends, Path, HTTPException, status
from app.dependencies import token_payload, TokenPayload, Permission
from ..controller import (
    PatientsController, 
    PatientDoesNotExistException,
    PatientDoesNotEmptyException    
)


def delete_patient(
    id: int = Path(...),
    patients: PatientsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.USERS_EDIT]))
) -> None:
    try:
        return patients.delete_patient(id)
    except PatientDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
    except PatientDoesNotEmptyException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
