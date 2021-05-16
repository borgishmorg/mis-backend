from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Date, Integer, String
from .base import Base
from .role import Role


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    role_id = Column(ForeignKey(Role.id))

    first_name = Column(String(80), nullable=False)
    surname = Column(String(80), nullable=False)
    patronymic = Column(String(80))
    birthdate = Column(Date)
    address = Column(String(255))
    phone = Column(String(15))
    email = Column(String(320))
    blocked = Column(Boolean, default=False, nullable=False)

    role = relationship(argument='Role')
