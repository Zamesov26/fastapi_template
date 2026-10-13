"""Создание и настройка ASGI-приложения."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.api.handlers.routers_v1 import api_router as v1_routers
from src.middlewares.setup import add_middlewares
from src.settings import Settings


def create_app(settings: Settings | None = None) -> FastAPI:
    """Создать и настроить экземпляр FastAPI."""
    current_settings = settings or Settings()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        """Управлять ресурсами при запуске и завершении приложения."""
        app.state.engine = create_async_engine(current_settings.db.url)
        app.state.session_maker = async_sessionmaker(
            app.state.engine, expire_on_commit=False
        )
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
    app.include_router(v1_routers, prefix='/api/v1')
    return app
