from typing import Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from app.models import Examination as ExaminationModel
from app.services import session_scope
from app.constants import Constants
from .schemas import Examination, Examinations, ExaminationIn


class ExaminationDoesNotExistException(Exception):

    def __init__(self, id: int) -> None:
        super().__init__(Constants.Examinations.EXAMINATION_DOES_NOT_EXIST_MSP.format(id=id))


class UserOrPatientDoesNotExistException(Exception):

    def __init__(self, user_id: int, patient_id: int) -> None:
        super().__init__(
            Constants
            .Examinations
            .USER_OR_PATIENT_DOES_NOT_EXIST_MSG
            .format(
                user_id=user_id, 
                patient_id=patient_id
            )
        )


class ExaminationsController:
    
    def get_examinations(
        self, 
        offset: int = 0, 
        limit: int = 50
    ) -> Examinations:
        with session_scope() as session:
            total = (
                session
                .query(ExaminationModel)
                .count()
            )
            examinations = (
                session
                .query(ExaminationModel)
                .options(
                    joinedload(ExaminationModel.patient),
                    joinedload(ExaminationModel.user),
                )
                .order_by(ExaminationModel.datetime.desc())
                .limit(limit)
                .offset(offset)
                .all()
            )
            return Examinations(
                total=total, 
                examinations=jsonable_encoder(examinations)
            )

    def search_examinations(
        self, 
        patient_id: int,
        offset: int = 0, 
        limit: int = 50
    ) -> Examinations:
        with session_scope() as session:
            total = (
                session
                .query(ExaminationModel)
                .filter_by(patient_id=patient_id)
                .count()
            )
            examinations = (
                session
                .query(ExaminationModel)
                .options(
                    joinedload(ExaminationModel.patient),
                    joinedload(ExaminationModel.user),
                )
                .filter_by(patient_id=patient_id)
                .order_by(ExaminationModel.datetime.desc())
                .limit(limit)
                .offset(offset)
                .all()
            )
            return Examinations(
                total=total, 
                examinations=jsonable_encoder(examinations)
            )

    def get_examination(
        self,
        id: int
    ) -> Examination:
        with session_scope() as session:
            examination: Optional[ExaminationModel] = session.get(
                ExaminationModel, 
                id, 
                (
                    joinedload(ExaminationModel.patient),
                    joinedload(ExaminationModel.user),
                )
            )
            if examination is None:
                raise ExaminationDoesNotExistException(id)
            return Examination(**jsonable_encoder(examination))

    def add_examination(
        self,
        examination_in: ExaminationIn
    ) -> Examination:
        with session_scope() as session:
            try:
                examination = ExaminationModel(**examination_in.dict())
                session.add(examination)
                session.flush()
            except IntegrityError:
                raise UserOrPatientDoesNotExistException(
                    user_id=examination_in.user_id,
                    patient_id=examination_in.patient_id
                )
            id = examination.id
        return self.get_examination(id)

    def update_examination(
        self,
        id: int,
        examination_in: ExaminationIn
    ) -> Examination:
        with session_scope() as session:
            try:
                examination: Optional[ExaminationModel] = session.get(ExaminationModel, id)
                if examination is None:
                    raise ExaminationDoesNotExistException(id)
                examination.patient_id = examination_in.patient_id
                examination.user_id = examination_in.user_id
                examination.complaints = examination_in.complaints
                examination.anamnesis = examination_in.anamnesis
                examination.objectively = examination_in.objectively
                examination.diagnosis = examination_in.diagnosis
                examination.recomendations = examination_in.recomendations
                session.flush()
            except IntegrityError:
                raise UserOrPatientDoesNotExistException(
                    user_id=examination_in.user_id,
                    patient_id=examination_in.patient_id
                )
        return self.get_examination(id)

    def delete_examination(self, id: int):
        with session_scope() as session:
            examination = session.get(ExaminationModel, id)
            if examination is None:
                raise ExaminationDoesNotExistException(id)
            session.delete(examination)
            session.flush()
