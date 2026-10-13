import pytest
from httpx import ASGITransport, AsyncClient
from src.main import create_app
from src.settings import Settings

from tests.settings import TestDBSettings


@pytest.fixture
def app():
    """Создать изолированный экземпляр приложения для теста."""
    return create_app(Settings(db=TestDBSettings()))


@pytest.fixture
async def client(app):
    """Создать HTTP-клиент без запуска жизненного цикла приложения."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as ac:
        yield ac

    app.dependency_overrides.clear()
