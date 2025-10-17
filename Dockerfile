# Use a Debian-based image instead of Alpine
FROM python:3.12-slim

# Prevent Python from writing .pyc files and buffer issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install build dependencies for pydantic-core and requests
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y build-essential gcc \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Copy the rest of your project
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start the app
CMD ["hypercorn", "main:app", "--bind", "localhost:8000"]
