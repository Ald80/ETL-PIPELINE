from fastapi import FastAPI, Depends, Query
from sqlalchemy import func, text
from sqlalchemy.orm import Session, load_only, class_mapper
from session_database_source import get_db
from models.data import Data
from datetime import datetime, timedelta
from session_database_source import Base, engine
from dateutil.parser import parse
from typing import List, Optional
from http import HTTPStatus
from fastapi import HTTPException

app = FastAPI() 

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return "hello"

@app.get("/get-data-source")
def get_data_target(date: datetime, is_wind_speed: bool, is_power: bool, is_ambient_temperature: bool,
    database: Session = Depends(get_db)):
    source_data = database.query(Data).filter()
    source_data_list = [{
        "timestamp": s.timestamp,
        "wind_speed": s.wind_speed,
        "power": s.power,
        "ambient_temprature": s.ambient_temprature}
        for s in source_data]
    return source_data_list

# @app.get("/get-data-source-by-parameter")
# def get_data_target_by_parameter(date_str: str, is_wind_speed: bool = False, is_power: bool = False, is_ambient_temperature: bool = False,
#     database: Session = Depends(get_db)):

#     # Data.timestamp, 
#     # Data.wind_speed if is_wind_speed, 
#     # Data.power, 
#     # Data.ambient_temprature
#     # date_formatted = datetime.strptime(date_str, '%d/%m/%Y')
#     # date_formatted = datetime.strptime(date_str, '%Y-%m-%d')
#     date_formatted = parse(date_str, dayfirst=True)

#     start_date_hour = datetime.combine(date_formatted, datetime.min.time())
#     end_date_hour = start_date_hour + timedelta(days=1) - timedelta(seconds=1)
#     # datetime.combine(date_formatted, datetime.)
#     print(start_date_hour)
#     print(end_date_hour)
#     params_dict = {"wind_speed": is_wind_speed, "power": is_power, "ambient_temperature": is_ambient_temperature}
#     fields: list = [key for key, value in params_dict.items() if value]
#     # for key, value in params_dict.items():
#     #     if value:
#     #         fields.append(key)
#     # source_data = database.query(Data).options(load_only(*fields)).filter(func.date(Data.timestamp) == date.date()).all()
#     # source_data = database.query(Data).options(load_only(*fields)).filter(func.strftime('%Y-%m-%d', Data.timestamp) == date_formatted.strftime('%Y-%m-%d')).all()
#     # source_data = database.query(Data).options(load_only(*fields)).filter(func.strftime('%Y-%m-%d', Data.timestamp) == date_formatted).all()
#     source_data = database.query(Data).options(load_only(*fields)).filter(Data.timestamp.between(start_date_hour, end_date_hour)).all()
#     source_data_list = [{
#         "timestamp": s.timestamp,
#         "wind_speed": s.wind_speed,
#         "power": s.power,
#         "ambient_temprature": s.ambient_temprature}
#         for s in source_data]
#     return source_data_list

# def row_to_dict(row):
#     return {c.key: getattr(row, c.key) for c in class_mapper(row.__class__).mapped_table.c}


# def row_to_dict(row):
#     return {c.key: getattr(row, c.key) for c in class_mapper(row.__class__).mapped_table.c}

@app.get("/get-data-source-by-parameter")
def get_data_target_by_parameter(date_str: str, variables: Optional[List[str]] = Query(None), database: Session = Depends(get_db)):
    if not variables:
        return HTTPException(status_code=404, detail="No variables provided") 
        
    # Data.timestamp, 
    # Data.wind_speed if is_wind_speed, 
    # Data.power, 
    # Data.ambient_temprature
    # date_formatted = datetime.strptime(date_str, '%d/%m/%Y')
    # date_formatted = datetime.strptime(date_str, '%Y-%m-%d')
    date_formatted = parse(date_str, dayfirst=True)

    start_date_hour = datetime.combine(date_formatted, datetime.min.time())
    end_date_hour = start_date_hour + timedelta(days=1) - timedelta(seconds=1)
    # datetime.combine(date_formatted, datetime.)
    print(start_date_hour)
    print(end_date_hour)
    # params_dict = {"wind_speed": is_wind_speed, "power": is_power, "ambient_temperature": is_ambient_temperature}
    # fields: list = [key for key, value in params_dict.items() if value]
    # for key, value in params_dict.items():
    #     if value:
    #         fields.append(key)
    # source_data = database.query(Data).options(load_only(*fields)).filter(func.date(Data.timestamp) == date.date()).all()
    # source_data = database.query(Data).options(load_only(*fields)).filter(func.strftime('%Y-%m-%d', Data.timestamp) == date_formatted.strftime('%Y-%m-%d')).all()
    # source_data = database.query(Data).options(load_only(*fields)).filter(func.strftime('%Y-%m-%d', Data.timestamp) == date_formatted).all()
    # source_data = database.query(Data).options(load_only(*fields)).filter(Data.timestamp.between(start_date_hour, end_date_hour)).all()
    query_srting: str = f"SELECT timestamp, {', '.join(variables)} FROM data WHERE timestamp BETWEEN :start_date_hour AND :end_date_hour"
    query = text(query_srting)
    # query = f"SELECT timestamp, {', '.join(variables)} FROM data WHERE timestamp BETWEEN %s AND %s"
    # source_data = database.query(Data).options(load_only(*fields)).filter(Data.timestamp.between(start_date_hour, end_date_hour)).all()
    params: dict[str, datetime] = {"start_date_hour": start_date_hour, "end_date_hour": end_date_hour}
    source_data = database.execute(query, params).fetchall()
    # query_string = f"SELECT timestamp, {', '.join(variables)} FROM data WHERE timestamp BETWEEN :start AND :end"
    # query = text(query_string)
    
    # Execute the query
    # result = database.execute(query, {"start": start, "end": end}).fetchall()
    # database.execute(query).
    # source_data_list = [{
        # "timestamp": s.timestamp,
        # "wind_speed": s.wind_speed,
        # "power": s.power,
        # "ambient_temprature": s.ambient_temprature
        # }
        # for s in source_data]
    # print(source_data)
    # return source_data.__dict__
    # return source_data_list
    # result_list = [dict(row) for row in source_data]
    # result_list = [row_to_dict(row) for row in source_data]
    return [dict(row._mapping) for row in source_data]


# def generate_data_target_dict():


