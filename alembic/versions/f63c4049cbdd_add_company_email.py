"""add company email

Revision ID: f63c4049cbdd
Revises: ce761818014a
Create Date: 2024-01-20 12:27:11.277563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f63c4049cbdd'
down_revision: Union[str, None] = 'ce761818014a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('traders', sa.Column('company_response_email', sa.String(), nullable=True))
    op.create_index(op.f('ix_traders_company_response_email'), 'traders', ['company_response_email'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_traders_company_response_email'), table_name='traders')
    op.drop_column('traders', 'company_response_email')
    # ### end Alembic commands ###
