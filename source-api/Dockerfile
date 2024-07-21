FROM python:3.12.4-slim-bullseye
WORKDIR /source-api
COPY ./requirements.txt ./requirements.txt
COPY ./db ./db
COPY ./models ./models 
COPY ./source-db-migration ./source-db-migration 
COPY ./alembic.ini ./alembic.ini
COPY ./main.py ./main.py 
COPY ./session_database_source.py ./session_database_source.py
COPY ./scripts/run_alembic.sh ./scripts/run_alembic.sh
RUN pip install -r requirements.txt
RUN chmod +x ./scripts/run_alembic.sh
CMD ./scripts/run_alembic.sh && uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info
