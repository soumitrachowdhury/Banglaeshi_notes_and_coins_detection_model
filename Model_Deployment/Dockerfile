# Useing the slim version to minimize disk space usage
FROM python:3.10-slim

# Setting the working directory inside the container
WORKDIR /app

# Install system dependencies required by OpenCV (used by Ultralytics)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copying requirements first to leverage Docker's layer caching
COPY requirements.txt .

# Installing Python dependencies (CPU-only versions) without caching to save space
RUN pip install --no-cache-dir -r requirements.txt

# Copying application code and the model into the container
COPY . .

# Exposing the port FastAPI will run on
EXPOSE 8000

# Commanding to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]