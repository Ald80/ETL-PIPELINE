"""insert_value_in_signal_table

Revision ID: 77648c5a920b
Revises: 0df07f315403
Create Date: 2024-07-20 19:37:37.930971

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision: str = '77648c5a920b'
down_revision: Union[str, None] = '0df07f315403'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

metadata = sa.MetaData()

signal_table = sa.Table(
    'signal',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String, nullable=False),
)


def upgrade() -> None:
    connection = op.get_bind()
    Session = sessionmaker(bind=connection)
    session = Session()

    signal = {'name': 'signal_1'}

    session.execute(signal_table.insert().values(signal))
    session.commit()
    session.close()


def downgrade() -> None:
    op.execute('TRUNCATE TABLE signal cascade;')
