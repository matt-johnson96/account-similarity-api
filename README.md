# FastAPI Account Similarity API

## Overview

This FastAPI application provides an API for finding similar accounts based on hashtag usage and account screen names.

## Prerequisites

```bash
# Python (version 3.9 recommended)
[Install Python](https://www.python.org/)

# Poetry for managing dependencies
pip install poetry

# Docker for containerization
[Install Docker](https://www.docker.com/)
```

## Standalone Installation and Run

```bash
# Clone the repository
git clone <repository-url>
cd <repository-directory>

# Install dependencies using Poetry
poetry install

# Run the FastAPI app
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000
```

The app will be accessible at http://localhost:8000.

## Containerized Deployment
```bash
# Build the Docker image
docker build -t account-similarity-api .

# Run the Docker container
docker run -p 8000:8000 account-similarity-api
```

The app will be accessible at http://localhost:8000.


## Cleanup
```bash
# To stop the standalone FastAPI app, press Ctrl + C.
# To stop and remove the Docker container
docker ps  # Find the CONTAINER_ID
docker stop CONTAINER_ID
```
