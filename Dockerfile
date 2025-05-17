# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gunicorn port
EXPOSE 8000

# Run Django via Gunicorn
CMD ["gunicorn", "django_app.wsgi:application", "--bind", "0.0.0.0:8000"]
