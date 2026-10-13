import pytest
from httpx import ASGITransport, AsyncClient
from src.database.settings import DBSettings
from src.dependencies import get_session
from src.main import create_app
from src.settings import Settings


@pytest.fixture
async def client(session_maker):
    """Создаём тестовый клиент с переопределённой зависимостью get_session."""
    app = create_app(Settings(db=DBSettings(name='test_db')))

    async def override_get_session():
        async with session_maker() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as ac:
        yield ac

    app.dependency_overrides.clear()
