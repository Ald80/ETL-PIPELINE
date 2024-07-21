"""insert random values in data table

Revision ID: 6053a5016d20
Revises: 8a0a9939e570
Create Date: 2024-07-20 20:36:17.303685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import random

# revision identifiers, used by Alembic.
revision: str = '6053a5016d20'
down_revision: Union[str, None] = '8a0a9939e570'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

metadata = sa.MetaData()

data_table = sa.Table(
    'data',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('timestamp', sa.DateTime, nullable=False),
    sa.Column('wind_speed', sa.Float, nullable=False),
    sa.Column('power', sa.Float, nullable=False),
    sa.Column('ambient_temperature', sa.Float, nullable=False),
)


def insert_random_target_data():
    connection = op.get_bind()
    Session = sessionmaker(bind=connection)
    session = Session()

    start_date = datetime(2023, 1, 1)
    end_date = start_date + timedelta(days=10)
    current_time = start_date

    while current_time < end_date:
        wind_speed = round(random.uniform(2, 30), 2) # velocidade do vento em m/s
        power = round(random.uniform(2, 500), 2) # Potência em megawatts
        ambient_temperature = round(random.uniform(20, 35), 1) # Temperatura ambiente

        data = {
            'timestamp': current_time,
            'wind_speed': wind_speed,
            'power': power,
            'ambient_temperature': ambient_temperature,
        }

        session.execute(data_table.insert().values(data))
        current_time += timedelta(minutes=1)

    session.commit()
    session.close()


def upgrade() -> None:
    insert_random_target_data()


def downgrade() -> None:
    op.execute('TRUNCATE TABLE data')
