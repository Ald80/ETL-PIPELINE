from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@source-database:5432/sourcedb"

engine = create_engine(DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
