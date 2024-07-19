from sqlalchemy import create_engine
from session_database_target import engine, Base
from models import signal, data

Base.metadata.create_all(bind=engine)
