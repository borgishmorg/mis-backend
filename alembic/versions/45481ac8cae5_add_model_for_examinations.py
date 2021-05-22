"""Add model for examinations

Revision ID: 45481ac8cae5
Revises: ed531e2efd68
Create Date: 2021-05-22 20:47:32.074759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45481ac8cae5'
down_revision = 'ed531e2efd68'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('examinations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('complaints', sa.String(length=1000), nullable=False),
    sa.Column('anamnesis', sa.String(length=1000), nullable=False),
    sa.Column('diagnosis', sa.String(length=1000), nullable=False),
    sa.Column('recomendations', sa.String(length=1000), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('examinations')
