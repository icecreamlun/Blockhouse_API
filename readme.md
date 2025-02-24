# Trade Orders API

A FastAPI-based backend service for handling trade orders with real-time updates via WebSocket.

## Features

- REST API endpoints for trade order management
- Real-time order updates via WebSocket
- SQLite database for data persistence
- Containerized deployment
- CI/CD pipeline with GitHub Actions

## Technical Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite
- **Containerization**: Docker
- **Deployment**: AWS EC2
- **CI/CD**: GitHub Actions

## API Endpoints

- `POST /orders`: Create a new trade order
- `GET /orders`: Retrieve all orders
- `WS /ws`: WebSocket endpoint for real-time updates

## Local Development

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run locally:

   ```bash
   uvicorn app.main:app --reload
   ```

## Docker Deployment

Build and run the container:

```bash
docker build -t blockhouse_api:latest .
docker run -d -p 8000:8000 blockhouse_api:latest
```

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── schemas.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Deployment

The service is deployed on AWS EC2 and accessible at:

```
http://18.212.27.22:8000/orders
```

## Assignment Overview

This project is part of the Blockhouse Work Trial Task, which involves building a simple backend service that:

- Exposes REST APIs for trade order management.
- Is containerized using Docker.
- Is deployed on an AWS EC2 instance.
- Has a CI/CD pipeline set up using GitHub Actions.

## Technical Requirements

### Backend Development (Python & Golang)

This backend service is implemented using FastAPI (Python) and provides:

- `POST /orders`: Accepts trade order details (symbol, price, quantity, order type).
- `GET /orders`: Returns a list of submitted orders.
- Data persistence using SQLite (can be extended to PostgreSQL).

**Bonus Feature:**
- WebSocket support for real-time order status updates.

### DevOps & Deployment (AWS EC2 + Docker)

#### Containerization
- The application is containerized using Docker.
- Docker Compose can be used for local multi-container setup (optional).

#### Deployment on AWS EC2
- The service is deployed on an Ubuntu-based EC2 instance.
- Docker and PostgreSQL are installed and configured on EC2.
- The containerized application runs on EC2.

#### CI/CD with GitHub Actions
- The GitHub Actions workflow includes:
  - Running tests on PRs.
  - Building the container image.
  - SSH-ing into the EC2 instance and deploying the latest version on merge to `main`.

## Expected Deliverables

- A well-structured GitHub repository with a detailed README.
- API documentation (Swagger/OpenAPI included).
- CI/CD pipeline configuration.
- A short video (5-10 min) explaining the solution and approach.

## Evaluation Criteria

- Clean, efficient backend code (Python/Golang).
- Proper use of Docker for deployment.
- Functioning CI/CD pipeline using GitHub Actions.
- API correctness and edge case handling.

The service is deployed on AWS EC2 and accessible at:

```
http://http://18.212.27.22:8000/
```

## API Documentation

Access the interactive API documentation at `/docs` endpoint.

### Example trade order:

```json
{
  "symbol": "AAPL",
  "price": 150.0,
  "quantity": 100,
  "order_type": "BUY"
}
