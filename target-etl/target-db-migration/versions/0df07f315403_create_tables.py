"""create_tables

Revision ID: 0df07f315403
Revises: 
Create Date: 2024-07-20 19:35:24.899547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0df07f315403'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'signal',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='signal_pkey'),
    )
    op.create_table(
        'data', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('timestamp',
                  postgresql.TIMESTAMP(timezone=True),
                  autoincrement=False,
                  nullable=True),
        sa.Column('signal_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('value', sa.Double(), autoincrement=False, nullable=True),
        sa.Column('power_mean', sa.Double(), autoincrement=False, nullable=True),
        sa.Column('power_min', sa.Double(), autoincrement=False, nullable=True),
        sa.Column('power_max', sa.Double(), autoincrement=False, nullable=True),
        sa.Column('power_std', sa.Double(), autoincrement=False, nullable=True),
        sa.Column('wind_speed_mean', sa.Double(), autoincrement=False, nullable=True),
        sa.Column('wind_speed_min', sa.Double(), autoincrement=False, nullable=True),
        sa.Column('wind_speed_max', sa.Double(), autoincrement=False, nullable=True),
        sa.Column('wind_speed_std', sa.Double(), autoincrement=False, nullable=True),
        sa.Column('ambient_temperature_mean',
                  sa.Double(),
                  autoincrement=False,
                  nullable=True),
        sa.Column('ambient_temperature_min',
                  sa.Double(),
                  autoincrement=False,
                  nullable=True),
        sa.Column('ambient_temperature_max',
                  sa.Double(),
                  autoincrement=False,
                  nullable=True),
        sa.Column('ambient_temperature_std',
                  sa.Double(),
                  autoincrement=False,
                  nullable=True),
        sa.ForeignKeyConstraint(['signal_id'], ['signal.id'],
                                name='data_signal_id_fkey'),
        sa.PrimaryKeyConstraint('id', name='data_pkey'))


def downgrade() -> None:
    op.drop_table('data')
    op.drop_table('signal')
