"""update user model to include trader id

Revision ID: 63936aea3bec
Revises: e7820df619f5
Create Date: 2024-01-03 15:28:33.375773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63936aea3bec'
down_revision: Union[str, None] = 'e7820df619f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('trader_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'users', 'traders', ['trader_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'trader_id')
    # ### end Alembic commands ###