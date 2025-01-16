FROM python:3.8.16-slim

WORKDIR /opt/data_dynamos_exercise

# COPY data_ingestion data_ingestion
COPY data_transformation data_transformation
COPY data_visualization data_visualization
COPY scripts/stearmlit_snowflake_startup.sh scripts/stearmlit_snowflake_startup.sh
COPY pyproject.toml poetry.toml ./

RUN apt-get update && \
    apt-get install --yes curl gcc git

ENV PATH=/root/.local/bin:$PATH

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.4 python3 - && \
    POETRY_VIRTUALENVS_CREATE=false && POETRY_HTTP_TIMEOUT=500 && \
    poetry env use python3.8 && \
    poetry config installer.parallel false && poetry install --no-interaction && \
    rm -rf ~/.cache/pypoetry/artifacts &&  \
    rm -rf ~/.cache/pypoetry/cache && \
    rm -rf ~/.cache/pip/* 
