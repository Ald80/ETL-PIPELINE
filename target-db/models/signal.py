from sqlalchemy import Column, Integer, String, Double, DateTime
from session_database_target import Base

class Signal(Base):
    __tablename__ = "signal"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    