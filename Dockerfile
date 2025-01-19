# Use a base Python 3.12 image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (including Tesseract)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of your application code into /app
COPY . /app

# Set the command to run your app
CMD ["python", "/app/main.py"]
