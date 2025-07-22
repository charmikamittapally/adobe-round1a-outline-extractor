# Use Python base image for amd64 architecture
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy Python app files
COPY app/ ./app/
COPY input/ ./input/
COPY output/ ./output/

# Install required Python libraries
RUN pip install --no-cache-dir -r app/requirements.txt

# Default command to run your script
CMD ["python", "app/main.py"]
