"""Add patient_id in examination model

Revision ID: b4c2236f1eb2
Revises: 45481ac8cae5
Create Date: 2021-05-22 21:11:06.886335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4c2236f1eb2'
down_revision = '45481ac8cae5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('examinations', sa.Column('patient_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'examinations', 'patients', ['patient_id'], ['id'])


def downgrade():
    op.drop_constraint(None, 'examinations', type_='foreignkey')
    op.drop_column('examinations', 'patient_id')
