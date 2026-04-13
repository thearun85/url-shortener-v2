FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry==2.3.1

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
&& poetry install --only main --no-root

COPY app/ ./app/

COPY scripts/ ./scripts/

COPY run.py .

EXPOSE 8080

CMD ["sh", "scripts/entrypoint.sh"]
