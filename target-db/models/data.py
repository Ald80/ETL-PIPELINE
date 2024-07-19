from sqlalchemy import Column, Integer, String, Double, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from session_database_target import Base
from models.signal import Signal

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True))
    signal_id = Column(Integer, ForeignKey(Signal.id))
    value = Column(Double)
    power_mean = Column(Double)
    power_min = Column(Double)
    power_max = Column(Double)
    power_std = Column(Double)
    wind_speed_mean = Column(Double)
    wind_speed_min = Column(Double)
    wind_speed_max = Column(Double)
    wind_speed_std = Column(Double)
    ambient_temprature_wind_speed_mean = Column(Double)
    ambient_temprature_wind_speed_min = Column(Double)
    ambient_temprature_wind_speed_max = Column(Double)
    ambient_temprature_wind_speed_std = Column(Double)
    signal = relationship("Signal")