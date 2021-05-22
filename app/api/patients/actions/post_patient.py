from fastapi import Depends
from app.dependencies import token_payload, TokenPayload, Permission
from ..controller import PatientsController
from ..schemas import PatientIn, Patient


def post_patient(
    patient_in: PatientIn,
    patients: PatientsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.PATIENTS_EDIT]))
) -> Patient:
    return patients.add_patient(patient_in)
