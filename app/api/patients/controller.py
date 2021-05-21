from typing import Optional
from fastapi.encoders import jsonable_encoder
from app.models import Patient as PatientModel
from app.services import session_scope
from app.constants import Constants
from .schemas import Patient, Patients, PatientIn


class PatientDoesNotExistException(Exception):

    def __init__(self, id: int) -> None:
        super().__init__(Constants.Patients.PATIENT_DOES_NOT_EXIST_MSP.format(id=id))


class PatientsController:
    
    def get_patients(self) -> Patients:
        with session_scope() as session:
            patients = (
                session
                .query(PatientModel)
                .all()
            )
            return Patients(patients=jsonable_encoder(patients))

    def get_patient(
        self,
        id: int
    ) -> Patient:
        with session_scope() as session:
            patient: Optional[PatientModel] = session.get(PatientModel, id)
            if patient is None:
                raise PatientDoesNotExistException(id)
            return Patient(**jsonable_encoder(patient))

    def add_patient(
        self,
        patient_in: PatientIn
    ) -> Patient:
        with session_scope() as session:
            patient = PatientModel(**patient_in.dict(exclude={'id'}))
            session.add(patient)
            session.flush()
            id = patient.id
        return self.get_patient(id)

    def update_patient(
        self,
        id: int,
        patient_in: PatientIn
    ) -> Patient:
        with session_scope() as session:
            patient: Optional[PatientModel] = session.get(PatientModel, id)
            if patient is None:
                raise PatientDoesNotExistException(id)
            patient.first_name = patient_in.first_name
            patient.surname = patient_in.surname
            patient.patronymic = patient_in.patronymic
            patient.sex = patient_in.sex
            patient.birthdate = patient_in.birthdate
            patient.address = patient_in.address
            patient.phone = patient_in.phone
            patient.email = patient_in.email
            session.flush()
        return self.get_patient(id)

    def delete_patient(self, id: int):
        with session_scope() as session:
            patient = session.get(PatientModel, id)
            if patient is None:
                raise PatientDoesNotExistException(id)
            session.delete(patient)
            session.flush()
