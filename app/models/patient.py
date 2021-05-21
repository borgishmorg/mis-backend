from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Date, Integer, String
from .base import Base


class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(80), nullable=False)
    surname = Column(String(80), nullable=False)
    patronymic = Column(String(80))
    sex = Column(Integer, nullable=False, default=0) # https://en.wikipedia.org/wiki/ISO/IEC_5218
    birthdate = Column(Date)
    address = Column(String(255))
    phone = Column(String(15))
    email = Column(String(320))
