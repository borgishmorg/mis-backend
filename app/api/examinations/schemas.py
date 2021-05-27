from enum import Enum
from datetime import datetime as DateTime
from pydantic import BaseModel, Field
from ..users.schemas import User
from ..patients.schemas import Patient


class ExaminationType(str, Enum):
    GENERAL = 'general'
    THERAPIST = 'therapist'
    SURGEON = 'surgeon'
    ORTHOPEDIST = 'orthopedist'


class ExaminationInBase(BaseModel):
    complaints: str = Field(max_length=1000)
    anamnesis: str = Field(max_length=1000)
    objectively: str = Field(max_length=1000)
    diagnosis: str = Field(max_length=1000)
    recomendations: str = Field(max_length=1000)
    user_id: int
    patient_id: int


class ExaminationIn(ExaminationInBase):
    type: ExaminationType = Field(ExaminationType.GENERAL, const=True)


class TherapistExaminationIn(ExaminationInBase):
    condition: str = Field(max_length=200)
    conscious: str = Field(max_length=200)
    cyanosis: str = Field(max_length=200)
    mucous: str = Field(max_length=200)
    food: str = Field(max_length=200)
    lymph_nodes: str = Field(max_length=200)
    rib_cage: str = Field(max_length=200)
    lungs: str = Field(max_length=200)
    breath: str = Field(max_length=200)
    heart: str = Field(max_length=200)
    tongue: str = Field(max_length=200)
    stomach: str = Field(max_length=200)
    liver: str = Field(max_length=200)
    kidneys: str = Field(max_length=200)
    swelling: str = Field(max_length=200)
    diuresis: str = Field(max_length=200)
    type: ExaminationType = Field(ExaminationType.THERAPIST, const=True)


class SurgeonExaminationIn(ExaminationInBase):
    condition: str = Field(max_length=200)
    stomach: str = Field(max_length=200)
    hernia: str = Field(max_length=200)
    operations: str = Field(max_length=200)
    trauma: str = Field(max_length=200)
    pathology: str = Field(max_length=200)
    type: ExaminationType = Field(ExaminationType.SURGEON, const=True)


class OrthopedistExaminationIn(ExaminationInBase):
    spine_axis: str = Field(max_length=100)
    upper_limb_axis: str = Field(max_length=100)
    lower_limb_axis: str = Field(max_length=100)
    asymmetry: str = Field(max_length=200)
    upper_limb_joints_functions: str = Field(max_length=100)
    lower_limb_joints_functions: str = Field(max_length=100)
    foot_deformation: str = Field(max_length=100)
    neurovascular_disorders: str = Field(max_length=200)
    type: ExaminationType = Field(ExaminationType.ORTHOPEDIST, const=True)


class ExaminationBase(ExaminationInBase):
    id: int
    datetime: DateTime
    user: User
    patient: Patient


class Examination(ExaminationBase, ExaminationIn):
    pass


class TherapistExamination(ExaminationBase, TherapistExaminationIn):
    pass


class SurgeonExamination(ExaminationBase, SurgeonExaminationIn):
    pass


class OrthopedistExamination(ExaminationBase, OrthopedistExaminationIn):
    pass


class ExaminationInfo(BaseModel):
    id: int
    datetime: DateTime
    type: ExaminationType
    user: User
    patient: Patient


class Examinations(BaseModel):
    total: int = 0
    examinations: list[ExaminationInfo] = list()
