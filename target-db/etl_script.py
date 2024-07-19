import httpx
import pandas as pd
from functools import reduce 
import sys
from session_database_target import engine

def extract(date):
    # API_URL = "localhost:8000/get-data-source/?data=2023/01/01&wind_speed=true&power=true&ambient_temprature=true"
    # API_URL = "localhost:8000/get-data-source-by-parameter?date_str=01-01-2023&variables=power&variables=wind_speed"
    API_URL = "http://localhost:8000/get-data-source-by-parameter"
    params = {"date_str": "01-01-2023", 'variables': ['power', 'wind_speed']}
    source_data = httpx.get(API_URL, params=params)
    # merged_dict = lambda x, y: {**x, **y}, source_data.json()
    # print(source_data.json())
    # print(merged_dict)
    # merged_dict = {}
    # for entry in source_data.json():
        # print(type(entry.keys()))
        # print(entry.values())

        
        # print(dict(zip(entry.keys(), entry.values())))
        # merged_dict.update(entry)
    
    # zip
    # for x in source_data.json():
    #     print(x)
    # return {x for x in source_data.json()}
    # print(merged_dict)
    data_frame = pd.DataFrame(source_data.json())
    # print(data_frame['timestamp'])
    
    data_frame['timestamp'] = pd.to_datetime(data_frame['timestamp'])

    data_frame.set_index('timestamp', inplace=True)
    # print(data_frame)
    agg_data_frame = data_frame.resample('10T').agg(['mean', 'min', 'max', 'std'])
    # print(agg_data_frame)
    agg_data_frame.columns = ['_'.join(col).strip() for col in agg_data_frame.columns.values]
    agg_data_frame['signal_id'] = 1
    agg_data_frame.to_sql('data', engine, if_exists="append", index=True)
    print(agg_data_frame)
    print(agg_data_frame.columns.to_list())
    return 1

def transform(source_data: dict):
    data_frame = pd.DataFrame(source_data)

def load():
    pass

def etl_process(date):
    source_data = extract(date)
    # transform(source_data)
    print(source_data)

if __name__=="__main__":
    date = sys.argv[1]
    etl_process(date)