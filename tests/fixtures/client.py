import pytest
from httpx import ASGITransport, AsyncClient
from src.database.settings import DBSettings
from src.main import create_app
from src.settings import Settings


@pytest.fixture
async def client():
    """Создать HTTP-клиент без запуска жизненного цикла приложения."""
    app = create_app(Settings(db=DBSettings(name='test_db')))

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as ac:
        yield ac
