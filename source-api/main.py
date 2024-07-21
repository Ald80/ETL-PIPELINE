from fastapi import FastAPI, Depends, Query
from fastapi import HTTPException
from sqlalchemy.orm import Session
from session_database_source import get_db
from datetime import datetime, timedelta
from session_database_source import Base, engine
from dateutil.parser import parse
from typing import List, Optional
from http import HTTPStatus
from db.source_db import fetch_source_data_by_parameter

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return "hello"


@app.get("/get-source-data-by-parameter")
def get_data_target_by_parameter(date_str: str,
                                 variables: Optional[List[str]] = Query(None),
                                 database: Session = Depends(get_db)):
    if not variables:
        return HTTPException(status_code=HTTPStatus.NOT_FOUND,
                             detail="No variables provided")

    date_formatted = parse(date_str, dayfirst=True)
    start_date_hour = datetime.combine(date_formatted, datetime.min.time())
    end_date_hour = start_date_hour + timedelta(days=1) - timedelta(seconds=1)
    source_data = fetch_source_data_by_parameter(start_date_hour, end_date_hour,
                                                 variables, database)
    return [dict(row._mapping) for row in source_data]
