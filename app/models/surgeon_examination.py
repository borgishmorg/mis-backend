from sqlalchemy import Column, String, ForeignKey
from .base import Base
from .examination import Examination


class SurgeonExamination(Base):
    __tablename__ = 'surgeon_examinations'

    id = Column(ForeignKey(Examination.id, ondelete="CASCADE"), primary_key=True)
    condition = Column(String(200), nullable=False, default='')
    stomach = Column(String(200), nullable=False, default='')
    hernia = Column(String(200), nullable=False, default='')
    operations = Column(String(200), nullable=False, default='')
    trauma = Column(String(200), nullable=False, default='')
    pathology = Column(String(200), nullable=False, default='')
