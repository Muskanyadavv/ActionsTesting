# 1. Base image with Python 3.11 installed
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements first to leverage Docker layer caching
COPY codeee/requirements.txt ./requirements.txt

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy source code and tests into the container
COPY codeee/src/ ./src/
COPY codeee/tests/ ./tests/

# 6. Set PYTHONPATH so Python can locate modules in src/
ENV PYTHONPATH=/app

# 7. Default command: run pytest when the container starts
CMD ["pytest", "-v", "tests/"]