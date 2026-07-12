FROM python:3.13.14-slim

RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-ron

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-root

COPY . .

RUN poetry install --only main --no-interaction

CMD ["uvicorn", "cfr_platforms.api:app", "--host", "0.0.0.0", "--port", "10000"]