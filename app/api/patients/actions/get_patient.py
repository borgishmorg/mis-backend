from fastapi import Depends, Path, HTTPException, status
from ..controller import PatientsController, PatientDoesNotExistException
from ..schemas import Patient


def get_patient(
    id: int = Path(...),
    patients: PatientsController = Depends()
) -> Patient:
    try:
        return patients.get_patient(id)
    except PatientDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
