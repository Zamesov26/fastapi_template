"""Проверять HTTP API состояния приложения."""

from unittest.mock import AsyncMock

import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.dependencies import get_session

pytestmark = pytest.mark.anyio


class TestLiveness:
    """Проверять endpoint состояния процесса приложения."""

    async def test_returns_alive_status(self, client):
        """Вернуть успешный статус работающего процесса."""
        response = await client.get('/api/v1/health/live')

        assert response.status_code == 200
        assert response.json() == {'status': 'alive'}


class TestReadiness:
    """Проверять endpoint готовности приложения."""

    async def test_returns_ready_when_database_is_available(
        self,
        app,
        client,
    ):
        """Вернуть готовность после успешного запроса к базе данных."""
        session = AsyncMock(spec=AsyncSession)

        async def override_get_session():
            yield session

        app.dependency_overrides[get_session] = override_get_session

        response = await client.get('/api/v1/health/ready')

        assert response.status_code == 200
        assert response.json() == {'status': 'ready'}
        session.execute.assert_awaited_once()

    async def test_returns_unavailable_when_database_query_fails(
        self,
        app,
        client,
    ):
        """Вернуть 503 при недоступности базы данных."""
        session = AsyncMock(spec=AsyncSession)
        session.execute.side_effect = SQLAlchemyError('database unavailable')

        async def override_get_session():
            yield session

        app.dependency_overrides[get_session] = override_get_session

        response = await client.get('/api/v1/health/ready')

        assert response.status_code == 503
        assert response.json() == {'detail': 'Database is unavailable'}
