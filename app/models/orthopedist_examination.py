from sqlalchemy import Column, String, ForeignKey
from .base import Base
from .examination import Examination


class OrthopedistExamination(Base):
    __tablename__ = 'orthopedist_examinations'

    id = Column(ForeignKey(Examination.id, ondelete="CASCADE"), primary_key=True)
    spine_axis = Column(String(100), nullable=False, default='')
    upper_limb_axis = Column(String(100), nullable=False, default='')
    lower_limb_axis = Column(String(100), nullable=False, default='')
    asymmetry = Column(String(200), nullable=False, default='')
    upper_limb_joints_functions = Column(String(100), nullable=False, default='')
    lower_limb_joints_functions = Column(String(100), nullable=False, default='')
    foot_deformation = Column(String(100), nullable=False, default='')
    neurovascular_disorders = Column(String(200), nullable=False, default='')
