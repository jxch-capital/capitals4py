FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential cmake meson ninja-build git && rm -rf /var/lib/apt/lists/* && pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --without dev

EXPOSE 8080

ENV DIR_PROJECT=/app
ENV ENV=prod
ENV PORT=8080

COPY . .
RUN poetry install --only-root

ENTRYPOINT ["sh", "-c", "poetry run uvicorn capitals4py.main:capitals4py --host 0.0.0.0 --port ${PORT}"]
