FROM python:3.9

RUN mkdir /app
WORKDIR /app

RUN apt-get update

COPY poetry.lock .
COPY pyproject.toml .
RUN apt-get update && pip install poetry \
    && poetry config virtualenvs.create false --local && poetry install

COPY . .