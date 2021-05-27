from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from .base import Base
from .user import User
from .patient import Patient


class Examination(Base):
    __tablename__ = 'examinations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, nullable=False, default=current_timestamp())
    complaints = Column(String(1000), nullable=False, default='')
    anamnesis = Column(String(1000), nullable=False, default='')
    objectively = Column(String(1000), nullable=False, default='')
    diagnosis = Column(String(1000), nullable=False, default='')
    recomendations = Column(String(1000), nullable=False, default='')
    user_id = Column(ForeignKey(User.id), nullable=False)
    patient_id = Column(ForeignKey(Patient.id), nullable=False)
    type = Column(String(20))

    user = relationship(User)
    patient = relationship(Patient)
