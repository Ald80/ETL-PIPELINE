import httpx
import pandas as pd
import sys
from session_database_target import engine, SessionLocal
from models.data import Signal


def get_id():
    database = SessionLocal()
    signal_name = 'signal_1'
    signal_data = database.query(Signal.id).filter(Signal.name == signal_name).first()
    signal_id = signal_data[0] if signal_data else None
    return signal_id


def extract(date):
    API_URL = 'http://source-api:8000/get-source-data-by-parameter'
    params = {"date_str": date, 'variables': ['power', 'wind_speed']}
    source_data = httpx.get(API_URL, params=params).json()
    return source_data


def transform(source_data, signal_id):
    data_frame = pd.DataFrame(source_data)
    data_frame['timestamp'] = pd.to_datetime(data_frame['timestamp'])
    data_frame.set_index('timestamp', inplace=True)
    agg_data_frame = data_frame.resample('10min').agg(['mean', 'min', 'max', 'std'])
    agg_data_frame.columns = [
        '_'.join(col).strip() for col in agg_data_frame.columns.values
    ]
    agg_data_frame['signal_id'] = signal_id
    return agg_data_frame


def load(agg_data_frame):
    try:
        agg_data_frame.to_sql('data', engine, if_exists='append', index=True)
    except Exception as e:
        print(e)


def etl_process(date):
    signal_id = get_id()
    source_data = extract(date)
    agg_data_frame = transform(source_data, signal_id)
    load(agg_data_frame)


if __name__ == "__main__":
    date = sys.argv[1]
    etl_process(date)
