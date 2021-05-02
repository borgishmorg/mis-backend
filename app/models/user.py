from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    login = Column('login', String(255), nullable=False, unique=True)
    password_hash = Column('password_hash', String(255), nullable=False)
