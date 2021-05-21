from fastapi import Depends
from ..controller import PatientsController
from ..schemas import PatientIn, Patient


def post_patient(
    patient_in: PatientIn,
    patients: PatientsController = Depends()
) -> Patient:
    return patients.add_patient(patient_in)
