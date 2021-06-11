import os
from typing import Optional
from fastapi import UploadFile, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload
from app.services.postgres import session_scope
from app.models import Research as ResearchModel
from .schemas import Research, Researches


class ResearchesController:

    FILES = 'files'

    def __init__(self) -> None:
        pass

    def add_research(
        self,
        research_file: UploadFile,
        user_id: int,
        patient_id: int,
        research_name: str
    ) -> Research:
        with session_scope() as session:
            research = ResearchModel(
                name=research_name,
                filetype=research_file.filename.split('.')[-1],
                user_id=user_id,
                patient_id=patient_id
            )
            session.add(research)
            session.flush()
            with open(f'{self.FILES}/{research.id}', 'wb') as file:
                file.write(research_file.file.read())
            session.commit()
            return self.get_research(research.id)

    def get_researches(
        self,
        patient_id: int,
        offset: int,
        limit: int,
    ) -> Researches:
        with session_scope() as session:
            total = (
                session
                .query(ResearchModel)
                .filter(ResearchModel.patient_id == patient_id)
                .count()
            )
            examinations = (
                session
                .query(ResearchModel)
                .options(
                    joinedload(ResearchModel.patient),
                    joinedload(ResearchModel.user),
                )
                .filter(ResearchModel.patient_id == patient_id)
                .order_by(ResearchModel.datetime.desc())
                .limit(limit)
                .offset(offset)
                .all()
            )
            return Researches(
                total=total,
                researches=jsonable_encoder(examinations)
            )

    def get_research(
        self,
        research_id: int
    ) -> Research:
        with session_scope() as session:
            research: Optional[ResearchModel] = session.get(
                ResearchModel,
                research_id
            )
            if research is None:
                raise HTTPException(status.HTTP_404_NOT_FOUND)
            return Research(
                **jsonable_encoder(research),
                user=jsonable_encoder(research.user),
                patient=jsonable_encoder(research.patient)
            )

    def delete_research(
        self,
        research_id: int
    ):
        with session_scope() as session:
            research: Optional[ResearchModel] = session.get(
                ResearchModel,
                research_id
            )
            if research is None:
                raise HTTPException(status.HTTP_404_NOT_FOUND)
            session.delete(research)
            os.remove(f'{self.FILES}/{research_id}')

    def get_research_file(
        self,
        research_id: int
    ) -> FileResponse:
        with session_scope() as session:
            research: Optional[ResearchModel] = session.get(
                ResearchModel,
                research_id
            )
            if research is None:
                raise HTTPException(status.HTTP_404_NOT_FOUND)
            return FileResponse(
                path=f'{self.FILES}/{research.id}',
                filename=f'{research.name}.{research.filetype}'
            )
