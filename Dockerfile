FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1

ENV \
  PYTHONUNBUFFERED 1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "uvicorn src.main:app --reload --host 0.0.0.0 --port 8000 --log-level ${APP_LOGLEVEL:-info} --use-colors"]
