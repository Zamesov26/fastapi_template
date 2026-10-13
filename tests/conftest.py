import pytest

from tests.fixtures.client import app, client
from tests.fixtures.db import clear_db, engine, session_maker

__all__ = ['app', 'session_maker', 'client', 'engine', 'clear_db']


@pytest.fixture(scope='session')
def anyio_backend():
    """Позволяет pytest использовать asyncio для async-тестов."""
    return 'asyncio'
