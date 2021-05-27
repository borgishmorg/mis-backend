from fastapi import Depends, Path, HTTPException, status
from app.dependencies import token_payload, TokenPayload, Permission
from ..controller import ExaminationsController, ExaminationDoesNotExistException


def delete_examination(
    id: int = Path(...),
    examinations: ExaminationsController = Depends(),
    token_payload: TokenPayload = Depends(token_payload())
) -> None:
    try:
        return examinations.delete_examination(id)
    except ExaminationDoesNotExistException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception)
        )
