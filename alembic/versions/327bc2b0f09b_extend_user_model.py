"""Extend user model

Revision ID: 327bc2b0f09b
Revises: 3ecd1f99f89c
Create Date: 2021-05-16 19:05:08.612652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '327bc2b0f09b'
down_revision = '3ecd1f99f89c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('first_name', sa.String(length=80), nullable=False))
    op.add_column('users', sa.Column('surname', sa.String(length=80), nullable=False))
    op.add_column('users', sa.Column('patronymic', sa.String(length=80), nullable=True))
    op.add_column('users', sa.Column('birthdate', sa.Date(), nullable=True))
    op.add_column('users', sa.Column('address', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('phone', sa.String(length=15), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=320), nullable=True))
    op.add_column('users', sa.Column('blocked', sa.Boolean(), nullable=True))


def downgrade():
    op.drop_column('users', 'blocked')
    op.drop_column('users', 'email')
    op.drop_column('users', 'phone')
    op.drop_column('users', 'address')
    op.drop_column('users', 'birthdate')
    op.drop_column('users', 'patronymic')
    op.drop_column('users', 'surname')
    op.drop_column('users', 'first_name')
