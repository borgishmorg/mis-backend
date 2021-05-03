from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer
from .base import Base
from .user import User
from .permission import Permission


class UserPermission(Base):
    __tablename__ = 'user_permissions'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', ForeignKey(User.id), nullable=False)
    permission_id = Column('permission_id', ForeignKey(Permission.id), nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'permission_id'),
    )
