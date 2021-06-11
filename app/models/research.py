from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from .base import Base
from .user import User
from .patient import Patient


class Research(Base):
    __tablename__ = 'researches'

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, nullable=False, default=current_timestamp())
    name = Column(String(100), nullable=False, default='')
    filetype = Column(String(10), nullable=False, default='')

    user_id = Column(ForeignKey(User.id), nullable=False)
    patient_id = Column(ForeignKey(Patient.id), nullable=False)

    user = relationship(User)
    patient = relationship(Patient)
