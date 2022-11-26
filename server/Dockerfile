# Image to be used
FROM python:3.8-slim-buster

# ENV PORT=8000

# install system dependencies
RUN apt-get update && apt-get install -y curl

# Install Poetry and project dependencies
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Work directory
WORKDIR /server

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev --no-root

COPY ./server /server
