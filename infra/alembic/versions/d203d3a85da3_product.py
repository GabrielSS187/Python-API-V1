"""product

Revision ID: d203d3a85da3
Revises: 
Create Date: 2023-05-12 20:40:39.626732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd203d3a85da3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'product',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100), unique=True, nullable=False),
        sa.Column('value', sa.Float(), nullable=False),
        sa.Column('type', sa.Enum('Recorrente', 'Avulso',
                  name='product_type'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('product')
