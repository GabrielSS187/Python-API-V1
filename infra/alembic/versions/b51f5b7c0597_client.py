"""client

Revision ID: b51f5b7c0597
Revises: 54711881543a
Create Date: 2023-05-12 21:06:59.694908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b51f5b7c0597'
down_revision = '54711881543a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'client',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('email', sa.String(length=120), unique=True, nullable=False),
        sa.Column('password', sa.String(length=120), nullable=False),
        sa.Column('account_id', sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(['account_id'], ['account.id'], ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_column('client')
