FROM python:3.12.4-slim-bullseye
WORKDIR /target-etl
COPY ./requirements.txt ./requirements.txt
COPY ./models ./models 
COPY ./target-db-migration ./target-db-migration 
COPY ./alembic.ini ./alembic.ini
COPY ./create_tables.py ./create_tables.py
COPY ./etl_script.py ./etl_script.py
RUN apt-get update && \
    apt-get install -y libpq-dev 
    # && \
    # apt-get install -y postgresql-devel

RUN pip install -r requirements.txt
COPY ./session_database_target.py ./session_database_target.py
COPY ./scripts/run_alembic.sh ./scripts/run_alembic.sh
# RUN chmod +x ./scripts/run_alembic.sh
# CMD sh -c "python create_tables.py && exec ./scripts/run_alembic.sh"
# CMD sh -c "exec python create_tables.py"
# CMD [ "python", "create_tables.py" ]
RUN chmod +x ./scripts/run_alembic.sh
# CMD sh -c "exec python create_tables.py && ./scripts/run_alembic.sh"
# CMD ./scripts/run_alembic.sh
ENTRYPOINT [ "sh", "-c", "./scripts/run_alembic.sh && tail -f /dev/null" ]