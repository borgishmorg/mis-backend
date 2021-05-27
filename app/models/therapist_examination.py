from sqlalchemy import Column, String, ForeignKey
from .base import Base
from .examination import Examination


class TherapistExamination(Base):
    __tablename__ = 'therapist_examinations'

    id = Column(ForeignKey(Examination.id, ondelete="CASCADE"), primary_key=True)
    condition = Column(String(200), nullable=False, default='')
    conscious = Column(String(200), nullable=False, default='')
    cyanosis = Column(String(200), nullable=False, default='')
    mucous = Column(String(200), nullable=False, default='')
    food = Column(String(200), nullable=False, default='')
    lymph_nodes = Column(String(200), nullable=False, default='')
    rib_cage = Column(String(200), nullable=False, default='')
    lungs = Column(String(200), nullable=False, default='')
    breath = Column(String(200), nullable=False, default='')
    heart = Column(String(200), nullable=False, default='')
    tongue = Column(String(200), nullable=False, default='')
    stomach = Column(String(200), nullable=False, default='')
    liver = Column(String(200), nullable=False, default='')
    kidneys = Column(String(200), nullable=False, default='')
    swelling = Column(String(200), nullable=False, default='')
    diuresis = Column(String(200), nullable=False, default='')
