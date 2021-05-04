from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
