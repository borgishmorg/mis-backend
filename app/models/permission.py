from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    code = Column('code', String(255), nullable=False, unique=True)
    name = Column('name', String(255), nullable=False)
