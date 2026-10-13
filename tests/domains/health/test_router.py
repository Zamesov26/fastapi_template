"""Проверять HTTP API состояния приложения."""

import pytest

pytestmark = pytest.mark.anyio


class TestHealthRouter:
    """Проверять контракт endpoint проверки доступности."""

    async def test_returns_healthy_status(self, client):
        """Вернуть успешный статус и ожидаемое состояние сервиса."""
        response = await client.get('/api/v1/health')

        assert response.status_code == 200
        assert response.json() == {
            'status': 'healthy',
            'message': 'FastAPI service is running',
        }
