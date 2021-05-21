"""Add patient model

Revision ID: ed531e2efd68
Revises: 327bc2b0f09b
Create Date: 2021-05-21 16:56:33.507999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed531e2efd68'
down_revision = '327bc2b0f09b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('patients',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('surname', sa.String(length=80), nullable=False),
    sa.Column('patronymic', sa.String(length=80), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=False, default=0),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=320), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('patients')
