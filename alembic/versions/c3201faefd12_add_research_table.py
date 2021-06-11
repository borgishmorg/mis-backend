"""Add research table

Revision ID: c3201faefd12
Revises: c45994e05371
Create Date: 2021-06-11 21:44:12.528662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3201faefd12'
down_revision = 'c45994e05371'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'researches',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('datetime', sa.DateTime(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('filetype', sa.String(length=10), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('patient_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('researches')
