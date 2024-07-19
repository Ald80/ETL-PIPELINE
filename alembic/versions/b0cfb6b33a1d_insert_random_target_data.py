"""Insert random target data

Revision ID: b0cfb6b33a1d
Revises: 
Create Date: 2024-07-16 17:15:15.144665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import random

# revision identifiers, used by Alembic.
revision: str = 'b0cfb6b33a1d'
down_revision: Union[str, None] = None
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
        # TODO Adjust random values ambient temperature 
        wind_speed = round(random.uniform(0, 30), 2) # velocidade do vento em m/s
        power = round(random.uniform(0, 1000), 2) # Potência em watts
        ambient_temperature = round(random.uniform(-10, 40), 2) # Temperatura ambiente

        data = {
            # 'date': current_time.date(),
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
    op.execute('DELETE FROM data')
