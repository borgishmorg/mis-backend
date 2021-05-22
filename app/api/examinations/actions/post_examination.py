from fastapi import Depends, status, HTTPException
from app.dependencies import token_payload, TokenPayload, Permission
from ..controller import ExaminationsController, UserOrPatientDoesNotExistException
from ..schemas import ExaminationIn, Examination


def post_examination(
    examination_in: ExaminationIn,
    examinations: ExaminationsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.EXAMINATIONS_EDIT]))
) -> Examination:
    try:
        return examinations.add_examination(examination_in)
    except UserOrPatientDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
