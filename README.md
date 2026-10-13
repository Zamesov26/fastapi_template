# FastAPI Base Template

A robust, production-ready FastAPI template designed to accelerate development of new projects with modern best practices and essential integrations out-of-the-box.

## 🚀 Features

- **FastAPI** - Modern, fast (high-performance) web framework for building APIs with Python
- **SQLAlchemy 2.0** - Modern SQL Toolkit and Object-Relational Mapping (ORM)
- **Async PostgreSQL** - Asynchronous database operations with PostgreSQL using asyncpg
- **Pydantic Settings** - Settings management with environment variable support
- **Dependency Injection** - Built-in dependency management
- **Database Migrations** - Alembic integration for database schema migrations
- **Structured Project Layout** - Clean architecture following best practices
- **Configuration Management** - Environment-based configuration with `.env` support
- **Middleware Support** - Extensible middleware system
- **Life Cycle Management** - Proper async engine disposal and session management

## 📁 Project Structure

```
fastapi_base_template/
├── .example.env          # Example environment variables
├── .gitignore           # Git ignore patterns
├── alembic.ini          # Alembic configuration
├── dev_run.py           # Development server runner
├── dev.requirements.txt # Development dependencies
├── requirements.txt     # Production dependencies
├── src/                 # Main application package
│   ├── __init__.py
│   ├── dependencies.py  # Dependency injection functions
│   ├── main.py          # Application entry point
│   ├── settings.py      # Main settings configuration
│   ├── api/            # API endpoints and routes
│   │   ├── __init__.py
│   │   ├── settings.py # API-specific settings
│   │   └── handlers/
│   │       ├── __init__.py
│   │       ├── life_handler.py # Health check endpoint
│   │       └── routers_v1.py # API v1 router
│   ├── database/       # Database configuration and models
│   │   ├── __init__.py
│   │   ├── base.py     # Base model class
│   │   ├── settings.py # Database settings
│   │   └── migrations/ # Alembic migrations
│   ├── middlewares/    # Application middleware
│   ├── models/         # SQLAlchemy models
│   └── schemas/        # Pydantic schemas
└── tests/              # Test suite
    ├── __init__.py
    ├── app/            # Application tests
    ├── fixtures/       # Test fixtures
    └── conftest.py     # Pytest configuration
```

## 🛠️ Installation

### Prerequisites

- Python 3.10+
- PostgreSQL database (for asyncpg)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi_base_template
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r dev.requirements.txt
```

4. Create your environment file:
```bash
cp .example.env .env
```

5. Configure your `.env` file with your specific settings:
```bash
# API Settings
API_NAME=My FastAPI App
API_DEBUG=True

# Database Settings
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=your_database_name
DB_DRIVER=asyncpg
```

## 🏃‍♂️ Running the Application

### Development

For development with auto-reload:

```bash
python dev_run.py
```

Or using uvicorn directly:
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

The application will be available at `http://0.0.0.0:8000`.

### Production

For production deployments:
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

Or using a production-ready ASGI server like Gunicorn:
```bash
gunicorn src.main:app -k uvicorn.workers.UvicornWorker
```

## 🧪 Testing

Run the test suite using pytest:

```bash
pytest
```

Or with more verbose output:
```bash
pytest -v
```

## 🗄️ Database Migrations

The template includes Alembic for database migrations:

1. Create a new migration:
```bash
alembic revision --autogenerate -m "description of changes"
```

2. Apply migrations:
```bash
alembic upgrade head
```

3. Check current migration status:
```bash
alembic current
```

## 🔧 Configuration

The application uses Pydantic Settings for configuration management:

- API settings (`API_` prefix in environment variables)
- Database settings (`DB_` prefix in environment variables)
- Settings are loaded from environment variables and .env files

### Available Settings

**API Settings:**
- `API_NAME` - Application name (default: "Application name API")
- `API_DEBUG` - Debug mode (default: False)
- `API_VERSION` - API version (default: "0.1.0")

**Database Settings:**
- `DB_HOST` - Database host (default: "localhost")
- `DB_PORT` - Database port (default: 5432)
- `DB_USER` - Database user (default: "postgres")
- `DB_PASSWORD` - Database password (default: "postgres")
- `DB_NAME` - Database name (required)
- `DB_DRIVER` - Database driver (default: "asyncpg")

## 🛡️ Security

This template provides a solid foundation for security:
- Input validation via Pydantic models
- Proper async context management
- Safe database connection handling
- Environment-based configuration to keep secrets secure

## 📊 API Endpoints

The template includes a health check endpoint:
- `GET /api/v1/health` - Returns application health status

## 🧩 Extending the Template

### Adding New Endpoints

1. Create new handlers in `src/api/handlers/`
2. Import and include them in `src/api/handlers/routers_v1.py`
3. Define your routes using FastAPI decorators

### Adding Models

1. Create new SQLAlchemy models in `src/models/`
2. Import them in `src/models/__init__.py`

### Adding Schemas

1. Create Pydantic schemas in `src/schemas/`
2. Use them for request/response validation

### Adding Middleware

1. Implement middleware in `src/middlewares/__init__.py`
2. Add them to the `add_middlewares` function

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - High-performance web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL Toolkit and ORM
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation library
- [Alembic](https://alembic.sqlalchemy.org/) - Database migration tool
