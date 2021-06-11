from datetime import datetime
from pydantic import BaseModel
from ..users.schemas import User
from ..patients.schemas import Patient


class Research(BaseModel):
    id: int
    datetime: datetime
    name: str
    filetype: str
    user: User
    patient: Patient


class Researches(BaseModel):
    total: int
    researches: list[Research]
