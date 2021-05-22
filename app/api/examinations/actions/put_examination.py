from fastapi import Depends, Path, HTTPException, status
from app.dependencies import token_payload, TokenPayload, Permission
from ..controller import (
    ExaminationsController, 
    ExaminationDoesNotExistException,
    UserOrPatientDoesNotExistException
)
from ..schemas import Examination, ExaminationIn


def put_examination(
    examination_in: ExaminationIn,
    id: int = Path(...),
    examinations: ExaminationsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.EXAMINATIONS_EDIT]))
) -> Examination:
    try:
        return examinations.update_examination(id, examination_in)
    except ExaminationDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
    except UserOrPatientDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exception)
        )
