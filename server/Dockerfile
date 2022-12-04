# Image to be used
FROM python:3.8-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container.
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

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

ENV PYTHONPATH=/server

RUN poetry install --no-dev --no-root

COPY . /server

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "main:server"]
