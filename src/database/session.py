"""Создание асинхронных компонентов доступа к базе данных."""

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool

from src.database.settings import DBSettings


def create_db_engine(
    settings: DBSettings,
    *,
    use_null_pool: bool = False,
) -> AsyncEngine:
    """Создать асинхронный engine для переданных настроек."""
    if use_null_pool:
        return create_async_engine(settings.url, poolclass=NullPool)
    return create_async_engine(settings.url)


def create_session_maker(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    """Создать фабрику асинхронных сессий."""
    return async_sessionmaker(engine, expire_on_commit=False)
