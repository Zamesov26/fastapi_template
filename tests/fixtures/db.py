import pytest
from src.database.base import Base
from src.database.session import create_db_engine, create_session_maker

from tests.settings import TestDBSettings


@pytest.fixture(scope='session')
async def engine():
    """Создаём движок и структуру таблиц один раз за все тесты."""
    engine = create_db_engine(TestDBSettings(), use_null_pool=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest.fixture(scope='session')
def session_maker(engine):
    """Создаём sessionmaker для тестов."""
    return create_session_maker(engine)


@pytest.fixture
async def clear_db(session_maker):
    """Очистить данные во всех таблицах перед тестом."""
    async with session_maker() as session:
        for table in reversed(Base.metadata.sorted_tables):
            await session.execute(table.delete())
        await session.commit()
