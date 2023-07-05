FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /base/

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN set -ex && pipenv install --system --dev

COPY . .