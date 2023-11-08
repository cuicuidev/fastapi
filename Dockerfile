# Use the official Python 3.10 image based on Alpine Linux
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install required system packages
RUN apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev && \
    apk add --no-cache libffi-dev libressl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

# Install uvicorn
RUN pip install uvicorn

# Copy your application code into the container
COPY . .

# Expose the port that your application will run on
EXPOSE 8000

# Command to run the server using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
