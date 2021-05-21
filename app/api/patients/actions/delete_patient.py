from fastapi import Depends, Path, HTTPException, status
from ..controller import PatientsController, PatientDoesNotExistException


def delete_patient(
    id: int = Path(...),
    patients: PatientsController = Depends()
) -> None:
    try:
        return patients.delete_patient(id)
    except PatientDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
