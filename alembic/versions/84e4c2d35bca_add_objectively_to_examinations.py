"""Add objectively to examinations

Revision ID: 84e4c2d35bca
Revises: b4c2236f1eb2
Create Date: 2021-05-27 13:38:49.098599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84e4c2d35bca'
down_revision = 'b4c2236f1eb2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('examinations', sa.Column('objectively', sa.String(length=1000), nullable=False, server_default=''))


def downgrade():
    op.drop_column('examinations', 'objectively')
