from typing import Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy import func, or_
from sqlalchemy.exc import IntegrityError
from app.models import Patient as PatientModel
from app.services import session_scope
from app.constants import Constants
from .schemas import Patient, Patients, PatientIn


class PatientDoesNotExistException(Exception):

    def __init__(self, id: int) -> None:
        super().__init__(Constants.Patients.PATIENT_DOES_NOT_EXIST_MSP.format(id=id))


class PatientDoesNotEmptyException(Exception):

    def __init__(self, id: int) -> None:
        super().__init__(Constants.Patients.PATIENT_DOES_NOT_EMPTY_MSP.format(id=id))


class PatientsController:
    
    def get_patients(
        self, 
        offset: int = 0, 
        limit: int = 50
    ) -> Patients:
        with session_scope() as session:
            total = (
                session
                .query(PatientModel)
                .count()
            )
            patients = (
                session
                .query(PatientModel)
                .order_by(
                    func.lower(PatientModel.surname),
                    func.lower(PatientModel.first_name),
                    func.lower(PatientModel.patronymic),
                )
                .limit(limit)
                .offset(offset)
                .all()
            )
            return Patients(
                total=total, 
                patients=jsonable_encoder(patients)
            )

    def search_patients(
        self, 
        q: str,
        offset: int = 0, 
        limit: int = 50
    ) -> Patients:
        words = [word.lower() for word in q.split()][:3]

        with session_scope() as session:
            query = session.query(PatientModel)

            for word in words[:-1]:
                query = query.filter(or_(
                    func.lower(PatientModel.first_name) == word,
                    func.lower(PatientModel.surname) == word,
                    func.lower(PatientModel.patronymic) == word
                ))

            if len(words) > 0:
                word = words[-1]
                query = query.filter(or_(
                    func.lower(PatientModel.first_name).like(f'{word}%'),
                    func.lower(PatientModel.surname).like(f'{word}%'),
                    func.lower(PatientModel.patronymic).like(f'{word}%')
                ))

            total = query.count()
            patients = (
                query
                .order_by(
                    func.lower(PatientModel.surname),
                    func.lower(PatientModel.first_name),
                    func.lower(PatientModel.patronymic),)
                .limit(limit)
                .offset(offset)
                .all()
            )
            return Patients(
                total=total, 
                patients=jsonable_encoder(patients)
            )

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
            try:
                session.delete(patient)
                session.flush()
            except IntegrityError:
                raise PatientDoesNotEmptyException(id)
