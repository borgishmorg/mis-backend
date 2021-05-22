from datetime import datetime as DateTime
from pydantic import BaseModel, Field
from ..users.schemas import User
from ..patients.schemas import Patient


class ExaminationIn(BaseModel):
    datetime: DateTime
    complaints: str = Field(max_length=1000)
    anamnesis: str = Field(max_length=1000)
    diagnosis: str = Field(max_length=1000)
    recomendations: str = Field(max_length=1000)
    user_id: int
    patient_id: int


class Examination(ExaminationIn):
    id: int
    user: User
    patient: Patient


class Examinations(BaseModel):
    total: int = 0
    examinations: list[Examination] = list()
