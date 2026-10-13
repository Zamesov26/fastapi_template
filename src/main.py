"""Создание и настройка ASGI-приложения."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.router import api_router
from src.database.session import create_db_engine, create_session_maker
from src.settings import Settings
from src.web.middlewares.setup import add_middlewares


def create_app(settings: Settings | None = None) -> FastAPI:
    """Создать и настроить экземпляр FastAPI."""
    current_settings = settings or Settings()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        """Управлять ресурсами при запуске и завершении приложения."""
        app.state.engine = create_db_engine(current_settings.db)
        app.state.session_maker = create_session_maker(app.state.engine)
        try:
            yield
        finally:
            await app.state.engine.dispose()

    app = FastAPI(
        title=current_settings.api.name,
        version=current_settings.api.version,
        debug=current_settings.api.debug,
        lifespan=lifespan,
    )

    add_middlewares(app)
    app.include_router(api_router, prefix='/api/v1')
    return app
