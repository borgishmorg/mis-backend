from fastapi import Depends
from ..controller import PatientsController
from ..schemas import Patients


def get_patients(
    patients: PatientsController = Depends()
) -> Patients:
    return patients.get_patients()
