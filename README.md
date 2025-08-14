# Rate Limiter Pro

A robust and scalable rate limiting service built with FastAPI, designed to handle high-throughput API rate limiting requirements.

## Features

- **High Performance**: Built with FastAPI for optimal performance
- **Scalable**: Redis-backed storage for horizontal scaling
- **Flexible**: Configurable rate limiting policies
- **Docker Ready**: Containerized deployment with Docker Compose
- **Database Migrations**: Alembic-based database schema management
- **Testing**: Comprehensive test suite with pytest

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL with Alembic migrations
- **Cache**: Redis
- **Containerization**: Docker & Docker Compose
- **Testing**: pytest

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.8+ (for local development)

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd rate-limiter-pro
   ```

2. Start the services:
   ```bash
   docker-compose up -d
   ```

3. The API will be available at `http://localhost:8000`

### Local Development

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables and start the application

## API Documentation

Once the service is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Configuration

The application can be configured through environment variables or configuration files. See `app/config.py` for available options.

## Testing

Run the test suite:

```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

[Add your license here]
