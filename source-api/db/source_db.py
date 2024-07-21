from sqlalchemy import text
from sqlalchemy.orm import Session
from datetime import datetime


def fetch_source_data_by_parameter(start_date_hour, end_date_hour, variables,
                                   database: Session):

    query_srting: str = f"SELECT timestamp, {', '.join(variables)} " + \
    "FROM data WHERE timestamp BETWEEN :start_date_hour AND :end_date_hour"
    query = text(query_srting)
    params: dict[str, datetime] = {
        "start_date_hour": start_date_hour,
        "end_date_hour": end_date_hour
    }
    source_data = database.execute(query, params).fetchall()
    return source_data
