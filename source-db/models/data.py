from sqlalchemy import Column, Integer, String, Double, DateTime
from session_database_source import Base

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True))
    wind_speed = Column(Double)
    power = Column(Double)
    ambient_temperature = Column(Double)