"""Add new examinations types

Revision ID: 6e027c0f657a
Revises: 84e4c2d35bca
Create Date: 2021-05-27 14:37:11.238959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e027c0f657a'
down_revision = '84e4c2d35bca'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('orthopedist_examinations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spine_axis', sa.String(length=100), nullable=False),
    sa.Column('upper_limb_axis', sa.String(length=100), nullable=False),
    sa.Column('lower_limb_axis', sa.String(length=100), nullable=False),
    sa.Column('asymmetry', sa.String(length=200), nullable=False),
    sa.Column('upper_limb_joints_functions', sa.String(length=100), nullable=False),
    sa.Column('lower_limb_joints_functions', sa.String(length=100), nullable=False),
    sa.Column('foot_deformation', sa.String(length=100), nullable=False),
    sa.Column('neurovascular_disorders', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['examinations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('surgeon_examinations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=200), nullable=False),
    sa.Column('stomach', sa.String(length=200), nullable=False),
    sa.Column('hernia', sa.String(length=200), nullable=False),
    sa.Column('operations', sa.String(length=200), nullable=False),
    sa.Column('trauma', sa.String(length=200), nullable=False),
    sa.Column('pathology', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['examinations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('therapist_examinations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=200), nullable=False),
    sa.Column('conscious', sa.String(length=200), nullable=False),
    sa.Column('cyanosis', sa.String(length=200), nullable=False),
    sa.Column('mucous', sa.String(length=200), nullable=False),
    sa.Column('food', sa.String(length=200), nullable=False),
    sa.Column('lymph_nodes', sa.String(length=200), nullable=False),
    sa.Column('rib_cage', sa.String(length=200), nullable=False),
    sa.Column('lungs', sa.String(length=200), nullable=False),
    sa.Column('breath', sa.String(length=200), nullable=False),
    sa.Column('heart', sa.String(length=200), nullable=False),
    sa.Column('tongue', sa.String(length=200), nullable=False),
    sa.Column('stomach', sa.String(length=200), nullable=False),
    sa.Column('liver', sa.String(length=200), nullable=False),
    sa.Column('kidneys', sa.String(length=200), nullable=False),
    sa.Column('swelling', sa.String(length=200), nullable=False),
    sa.Column('diuresis', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['examinations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('examinations', sa.Column('type', sa.String(length=20), nullable=True))


def downgrade():
    op.drop_column('examinations', 'type')
    op.drop_table('therapist_examinations')
    op.drop_table('surgeon_examinations')
    op.drop_table('orthopedist_examinations')
