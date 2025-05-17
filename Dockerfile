# Use official Python base image
FROM python:3.13.3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies (for psycopg2 etc.)
RUN apt-get update \
  && apt-get install -y gcc libpq-dev git \
  && pip install --upgrade pip

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt \
  && apt-get remove -y gcc git \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Copy .env file
COPY .env .env

# Gunicorn command
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
