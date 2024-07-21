FROM python:3.12.4-slim-bullseye
WORKDIR /target-etl
COPY ./requirements.txt ./requirements.txt
COPY ./models ./models 
COPY ./target-db-migration ./target-db-migration 
COPY ./alembic.ini ./alembic.ini
COPY ./etl_script.py ./etl_script.py
COPY ./session_database_target.py ./session_database_target.py
COPY ./scripts/run_alembic.sh ./scripts/run_alembic.sh
RUN apt-get update && \
    apt-get install -y libpq-dev 
RUN pip install -r requirements.txt
RUN chmod +x ./scripts/run_alembic.sh
ENTRYPOINT [ "sh", "-c", "./scripts/run_alembic.sh && tail -f /dev/null" ]