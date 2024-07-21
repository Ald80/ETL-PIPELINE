"""Create table data

Revision ID: 8a0a9939e570
Revises: 
Create Date: 2024-07-20 20:29:06.008467

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8a0a9939e570'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'data', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('timestamp',
                  postgresql.TIMESTAMP(timezone=True),
                  autoincrement=False,
                  nullable=True),
        sa.Column('wind_speed', sa.Float, autoincrement=False, nullable=True),
        sa.Column('power', sa.Float(), autoincrement=False, nullable=True),
        sa.Column('ambient_temperature', sa.Float(), autoincrement=False,
                  nullable=True), sa.PrimaryKeyConstraint('id', name='data_pkey'))


def downgrade() -> None:
    op.drop_table('data')
