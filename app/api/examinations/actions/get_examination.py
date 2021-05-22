from fastapi import Depends, Path, HTTPException, status
from app.dependencies import token_payload, TokenPayload, Permission
from ..controller import ExaminationsController, ExaminationDoesNotExistException
from ..schemas import Examination


def get_examination(
    id: int = Path(...),
    examinations: ExaminationsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload(permissions=[Permission.EXAMINATIONS_VIEW]))
) -> Examination:
    try:
        return examinations.get_examination(id)
    except ExaminationDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
