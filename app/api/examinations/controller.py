from typing import Optional, Union
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from app.models import (
    Examination as ExaminationModel,
    TherapistExamination as TherapistExaminationModel,
    SurgeonExamination as SurgeonExaminationModel,
    OrthopedistExamination as OrthopedistExaminationModel
)
from app.dependencies import TokenPayload, token_payload, Permission, ForbiddenException
from app.services import session_scope
from app.constants import Constants
from .schemas import (
    Examination,
    TherapistExamination,
    SurgeonExamination,
    OrthopedistExamination,
    ExaminationIn, 
    TherapistExaminationIn,
    SurgeonExaminationIn, 
    OrthopedistExaminationIn, 
    ExaminationType,
    Examinations, 
)


class ExaminationDoesNotExistException(Exception):

    def __init__(self, id: int) -> None:
        super().__init__(Constants.Examinations.EXAMINATION_DOES_NOT_EXIST_MSP.format(id=id))


class WrongExaminationTypeException(Exception):

    def __init__(self, id: int) -> None:
        super().__init__(Constants.Examinations.WRONG_EXAMIANTION_TYPE_MSP.format(id=id))


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


EXAMINATIONS_COLUMNS = {
    'complaints', 'anamnesis', 'objectively',
    'diagnosis', 'recomendations','type',
    'user_id', 'patient_id'
}


class ExaminationsController:
    
    def __init__(
        self,
        token_payload: TokenPayload = Depends(token_payload())
    ) -> None:
        self.view_examinations_types: list[ExaminationType] = []
        self.edit_examinations_types: list[ExaminationType] = []

        if Permission.EXAMINATIONS_VIEW in token_payload.user.permissions:
            self.view_examinations_types.append(ExaminationType.GENERAL)
        if Permission.THERAPIST_EXAMINATIONS_VIEW in token_payload.user.permissions:
            self.view_examinations_types.append(ExaminationType.THERAPIST)
        if Permission.SURGEON_EXAMINATIONS_VIEW in token_payload.user.permissions:
            self.view_examinations_types.append(ExaminationType.SURGEON)
        if Permission.ORTHOPEDIST_EXAMINATIONS_VIEW in token_payload.user.permissions:
            self.view_examinations_types.append(ExaminationType.ORTHOPEDIST)

        if Permission.EXAMINATIONS_EDIT in token_payload.user.permissions:
            self.edit_examinations_types.append(ExaminationType.GENERAL)
        if Permission.THERAPIST_EXAMINATIONS_EDIT in token_payload.user.permissions:
            self.edit_examinations_types.append(ExaminationType.THERAPIST)
        if Permission.SURGEON_EXAMINATIONS_EDIT in token_payload.user.permissions:
            self.edit_examinations_types.append(ExaminationType.SURGEON)
        if Permission.ORTHOPEDIST_EXAMINATIONS_EDIT in token_payload.user.permissions:
            self.edit_examinations_types.append(ExaminationType.ORTHOPEDIST)


    def get_examinations(
        self, 
        offset: int = 0, 
        limit: int = 50
    ) -> Examinations:
        if len(self.view_examinations_types) == 0:
            raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
        with session_scope() as session:
            total = (
                session
                .query(ExaminationModel)
                .filter(ExaminationModel.type.in_(self.view_examinations_types))
                .count()
            )
            examinations = (
                session
                .query(ExaminationModel)
                .options(
                    joinedload(ExaminationModel.patient),
                    joinedload(ExaminationModel.user),
                )
                .filter(ExaminationModel.type.in_(self.view_examinations_types))
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
        if len(self.view_examinations_types) == 0:
            raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
        with session_scope() as session:
            total = (
                session
                .query(ExaminationModel)
                .filter(ExaminationModel.type.in_(self.view_examinations_types))
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
                .filter(ExaminationModel.type.in_(self.view_examinations_types))
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
    ) -> Union[Examination, TherapistExamination, SurgeonExamination, OrthopedistExamination]:
        if len(self.view_examinations_types) == 0:
            raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
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
            if examination.type not in self.view_examinations_types:
                raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
            examination = jsonable_encoder(examination)
            if examination['type'] == ExaminationType.THERAPIST:
                examination_extra: Optional[TherapistExaminationModel] = session.get(TherapistExaminationModel, id)
                if examination_extra is None:
                    raise ExaminationDoesNotExistException(id)
                examination.update(jsonable_encoder(examination_extra))
                return TherapistExamination(**examination)
            elif examination['type'] == ExaminationType.SURGEON:
                examination_extra: Optional[SurgeonExaminationModel] = session.get(SurgeonExaminationModel, id)
                if examination_extra is None:
                    raise ExaminationDoesNotExistException(id)
                examination.update(jsonable_encoder(examination_extra))
                return SurgeonExamination(**examination)
            elif examination['type'] == ExaminationType.ORTHOPEDIST:
                examination_extra: Optional[OrthopedistExaminationModel] = session.get(OrthopedistExaminationModel, id)
                if examination_extra is None:
                    raise ExaminationDoesNotExistException(id)
                examination.update(jsonable_encoder(examination_extra))
                return OrthopedistExamination(**examination)
            return Examination(**examination)

    def add_examination(
        self,
        examination_in: Union[ExaminationIn, TherapistExaminationIn, SurgeonExaminationIn, OrthopedistExaminationIn]
    ) -> Union[Examination, TherapistExamination, SurgeonExamination, OrthopedistExamination]:
        if examination_in.type not in self.edit_examinations_types:
            raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
        with session_scope() as session:
            try:
                examination = ExaminationModel(**examination_in.dict(include=EXAMINATIONS_COLUMNS))
                session.add(examination)
                session.flush()
                if examination_in.type == ExaminationType.THERAPIST:
                    examination_extra = TherapistExaminationModel(
                        id=examination.id,
                        **examination_in.dict(exclude=EXAMINATIONS_COLUMNS)
                    )
                    session.add(examination_extra)
                elif examination_in.type == ExaminationType.SURGEON:
                    examination_extra = SurgeonExaminationModel(
                        id=examination.id,
                        **examination_in.dict(exclude=EXAMINATIONS_COLUMNS)
                    )
                    session.add(examination_extra)
                elif examination_in.type == ExaminationType.ORTHOPEDIST:
                    examination_extra = OrthopedistExaminationModel(
                        id=examination.id,
                        **examination_in.dict(exclude=EXAMINATIONS_COLUMNS)
                    )
                    session.add(examination_extra)
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
        examination_in: Union[ExaminationIn, TherapistExaminationIn, SurgeonExaminationIn, OrthopedistExaminationIn]
    ) -> Union[Examination, TherapistExamination, SurgeonExamination, OrthopedistExamination]:
        if examination_in.type not in self.edit_examinations_types:
            raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
        with session_scope() as session:
            try:
                examination: Optional[ExaminationModel] = session.get(ExaminationModel, id)
                if examination is None:
                    raise ExaminationDoesNotExistException(id)
                if examination.type not in self.edit_examinations_types:
                    raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
                if examination.type != examination_in.type:
                    raise WrongExaminationTypeException(id)
                examination.patient_id = examination_in.patient_id
                examination.user_id = examination_in.user_id
                examination.complaints = examination_in.complaints
                examination.anamnesis = examination_in.anamnesis
                examination.objectively = examination_in.objectively
                examination.diagnosis = examination_in.diagnosis
                examination.recomendations = examination_in.recomendations
                if examination_in.type == ExaminationType.THERAPIST:
                    session.query(
                        TherapistExaminationModel
                    ).filter_by(
                        id=id
                    ).update(
                        examination_in.dict(exclude=EXAMINATIONS_COLUMNS)
                    )
                elif examination_in.type == ExaminationType.SURGEON:
                    session.query(
                        SurgeonExaminationModel
                    ).filter_by(
                        id=id
                    ).update(
                        examination_in.dict(exclude=EXAMINATIONS_COLUMNS)
                    )
                elif examination_in.type == ExaminationType.ORTHOPEDIST:
                    session.query(
                        OrthopedistExaminationModel
                    ).filter_by(
                        id=id
                    ).update(
                        examination_in.dict(exclude=EXAMINATIONS_COLUMNS)
                    )
                session.flush()
            except IntegrityError:
                raise UserOrPatientDoesNotExistException(
                    user_id=examination_in.user_id,
                    patient_id=examination_in.patient_id
                )
        return self.get_examination(id)

    def delete_examination(self, id: int):
        if len(self.edit_examinations_types) == 0:
            raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
        with session_scope() as session:
            examination = session.get(ExaminationModel, id)
            if examination is None:
                raise ExaminationDoesNotExistException(id)
            if examination.type not in self.edit_examinations_types:
                raise ForbiddenException(Constants.Token.FORBIDDEN_MSG)
            session.delete(examination)
            session.flush()
