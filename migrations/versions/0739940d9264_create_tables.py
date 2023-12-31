"""create tables

Revision ID: 0739940d9264
Revises: 
Create Date: 2023-12-22 17:49:17.695762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0739940d9264'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('patronymic', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('dismissed', 'tmp_not_working', 'work', name='status'), nullable=False),
    sa.Column('category', sa.Enum('driver', 'courier', name='category'), nullable=False),
    sa.Column('document', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('phones',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('employee_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('phones')
    op.drop_table('employees')
    # ### end Alembic commands ###
