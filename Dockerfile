# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for psycopg2
RUN apt-get update && apt-get install -y libpq-dev

# Install psycopg2 using pip
RUN pip install psycopg2

# Copy your Python application code to the container's working directory
COPY . /app

# Define the command to run your Python application
CMD ["python", "your_app.py"]
