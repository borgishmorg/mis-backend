from enum import IntEnum
from typing import Optional
from datetime import date
from pydantic import BaseModel, Field


class Sex(IntEnum):
    '''
    Sex:

    - Not known - 0
    - Male - 1
    - Female - 2
    - Not applicable - 9

    https://en.wikipedia.org/wiki/ISO/IEC_5218
    '''

    NOT_KNOWN = 0
    MALE = 1
    FEMALE = 2
    NOT_APPLICABLE = 9


class PatientIn(BaseModel):
    first_name: str = Field(max_length=80)
    surname: str = Field(max_length=80)
    patronymic: Optional[str] = Field(None, max_length=80)
    sex: Optional[Sex] = Sex.NOT_KNOWN
    birthdate: Optional[date] = None
    address: Optional[str] = Field(None, max_length=255)
    phone: Optional[str] = Field(None, max_length=15)
    email: Optional[str] = Field(None, max_length=320)


class Patient(PatientIn):
    id: int


class Patients(BaseModel):
    patients: list[Patient] = list()
