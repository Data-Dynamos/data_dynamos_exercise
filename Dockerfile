FROM python:3.8.16-slim

WORKDIR /opt/data_dynamos_exercise

# COPY data_ingestion data_ingestion
COPY data_transformation data_transformation
COPY data_visualization data_visualization
COPY pyproject.toml poetry.lock poetry.toml ./

RUN apt-get update && \
    apt-get install --yes curl gcc git

ENV PATH=/root/.local/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 - --yes && \
    POETRY_VIRTUALENVS_CREATE=false poetry install --no-interaction && \
    rm -rf ~/.cache/pypoetry/artifacts &&  \
    rm -rf ~/.cache/pypoetry/cache && \
    rm -rf ~/.cache/pip/* && \
    # dbt deps --project-dir data_ingestion && \
    dbt deps --project-dir data_transformation
