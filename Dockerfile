FROM python:3.11-slim

WORKDIR /app

# Install curl dan unzip (dibutuhkan Reflex)
RUN apt-get update && apt-get install -y curl unzip

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file ke dalam container
COPY . .
