"""Add user model

Revision ID: 6408529a3a8d
Revises: 
Create Date: 2021-05-02 14:13:41.129024

"""
from alembic import op
import sqlalchemy as sa
from app.hash import generate_password_hash


# revision identifiers, used by Alembic.
revision = '6408529a3a8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    users = op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('login', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    query = sa.insert(users).values([
        {
            'login': 'admin', 
            'password_hash': generate_password_hash('admin').hex()
        },
        {
            'login': 'user', 
            'password_hash': generate_password_hash('user').hex()
        }
    ])
    op.execute(query)


def downgrade():
    op.drop_table('users')
