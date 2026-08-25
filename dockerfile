FROM python:3.11-slim

WORKDIR /app

COPY codeee/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY codeee/src/ ./src/
COPY codeee/tests/ ./tests/

ENV PYTHONPATH=/app

CMD ["pytest", "-v", "tests/"]