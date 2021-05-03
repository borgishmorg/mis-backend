from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(255), nullable=False, unique=True)
    name_rus = Column('name_rus', String(255), nullable=False)
