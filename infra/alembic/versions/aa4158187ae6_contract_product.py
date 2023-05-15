"""contract_product

Revision ID: aa4158187ae6
Revises: b51f5b7c0597
Create Date: 2023-05-14 16:48:31.234069

"""
import uuid
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa4158187ae6'
down_revision = 'b51f5b7c0597'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'contract_product',
        sa.Column('id', sa.String(length=255), primary_key=True, nullable=False),
        sa.Column('account_id', sa.String(length=255), sa.ForeignKey('account.id'), nullable=False),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('product.id'), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_column('contract_product')
