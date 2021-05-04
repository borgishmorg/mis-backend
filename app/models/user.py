from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base
from .role import Role


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    role_id = Column(ForeignKey(Role.id))

    role = relationship(argument='Role')
