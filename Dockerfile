# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy only the pyproject.toml and poetry.lock to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install regular dependencies (non-development dependencies)
RUN pip install poetry && poetry install --no-dev

# Copy the main application code from src/
COPY src/ /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV FASTAPI_ENV production

# Command to run your application
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
