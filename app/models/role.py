from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class Role(Base):
    __tablename__ = 'roles'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    code = Column('code', String(255), nullable=False, unique=True)
    name = Column('name', String(255), nullable=False)

    permissions = relationship(
        argument='Permission',
        secondary='role_permissions'
    )
