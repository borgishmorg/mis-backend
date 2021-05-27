from typing import Union
from fastapi import Depends, status, HTTPException
from app.dependencies import token_payload, TokenPayload, Permission
from ..controller import ExaminationsController, UserOrPatientDoesNotExistException
from ..schemas import (
    Examination,
    TherapistExamination,
    SurgeonExamination,
    OrthopedistExamination,
    ExaminationIn, 
    TherapistExaminationIn,
    SurgeonExaminationIn,
    OrthopedistExaminationIn,
)


def post_examination(
    examination_in: Union[ExaminationIn, TherapistExaminationIn, SurgeonExaminationIn, OrthopedistExaminationIn],
    examinations: ExaminationsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.EXAMINATIONS_EDIT]))
) -> Union[Examination, TherapistExamination, SurgeonExamination, OrthopedistExamination]:
    try:
        return examinations.add_examination(examination_in)
    except UserOrPatientDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
