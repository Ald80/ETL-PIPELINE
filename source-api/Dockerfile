FROM python:3.12.4-slim-bullseye
WORKDIR /source-api
COPY ./requirements.txt ./requirements.txt
COPY ./models ./models 
COPY ./source-db-migration ./source-db-migration 
# COPY ./create_tables.py ./create_tables.py
COPY ./initialize_database.py ./initialize_database.py
COPY ./alembic.ini ./alembic.ini
COPY ./main.py ./main.py 
RUN pip install -r requirements.txt
COPY ./session_database_source.py ./session_database_source.py
COPY ./scripts/run_alembic.sh ./scripts/run_alembic.sh
RUN chmod +x ./scripts/run_alembic.sh
# CMD sh -c "./scripts/run_alembic.sh && exec uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info --reload" 
# CMD python initialize_database.py && ./scripts/run_alembic.sh && uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info
CMD ./scripts/run_alembic.sh && uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info
# CMD uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info && ./scripts/run_alembic.sh