"""Add on delete cascade for new examinations

Revision ID: c45994e05371
Revises: 6e027c0f657a
Create Date: 2021-05-27 16:49:59.233898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c45994e05371'
down_revision = '6e027c0f657a'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('orthopedist_examinations_id_fkey', 'orthopedist_examinations', type_='foreignkey')
    op.create_foreign_key(None, 'orthopedist_examinations', 'examinations', ['id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('surgeon_examinations_id_fkey', 'surgeon_examinations', type_='foreignkey')
    op.create_foreign_key(None, 'surgeon_examinations', 'examinations', ['id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('therapist_examinations_id_fkey', 'therapist_examinations', type_='foreignkey')
    op.create_foreign_key(None, 'therapist_examinations', 'examinations', ['id'], ['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint(None, 'therapist_examinations', type_='foreignkey')
    op.create_foreign_key('therapist_examinations_id_fkey', 'therapist_examinations', 'examinations', ['id'], ['id'])
    op.drop_constraint(None, 'surgeon_examinations', type_='foreignkey')
    op.create_foreign_key('surgeon_examinations_id_fkey', 'surgeon_examinations', 'examinations', ['id'], ['id'])
    op.drop_constraint(None, 'orthopedist_examinations', type_='foreignkey')
    op.create_foreign_key('orthopedist_examinations_id_fkey', 'orthopedist_examinations', 'examinations', ['id'], ['id'])
