from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer
from .base import Base
from .role import Role
from .permission import Permission


class RolePermission(Base):
    __tablename__ = 'role_permissions'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    role_id = Column('role_id', ForeignKey(Role.id), nullable=False)
    permission_id = Column('permission_id', ForeignKey(Permission.id), nullable=False)

    __table_args__ = (
        UniqueConstraint('role_id', 'permission_id'),
    )
