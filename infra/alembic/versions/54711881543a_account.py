"""account

Revision ID: 54711881543a
Revises: d203d3a85da3
Create Date: 2023-05-12 20:50:21.666163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54711881543a'
down_revision = 'd203d3a85da3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.String(length=255), nullable=False),
        sa.Column('name_account', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_account'))
    )


def downgrade() -> None:
    op.drop_table('account')
