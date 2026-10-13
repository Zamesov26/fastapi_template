"""Настройки тестового окружения."""

from pydantic import Field
from pydantic_settings import SettingsConfigDict
from src.database.settings import DBSettings


class TestDBSettings(DBSettings):
    """Настройки отдельной базы данных для интеграционных тестов."""

    model_config = SettingsConfigDict(env_prefix='TEST_DB_')

    name: str = Field('test_db')
