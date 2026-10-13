"""Настройки подключения к базе данных."""

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from src.config import AppBaseSettings


class DBSettings(AppBaseSettings):
    """Настройки подключения к базе данных."""

    model_config = SettingsConfigDict(env_prefix='DB_')

    host: str = Field('localhost')
    port: int = Field(5432)
    user: str = Field('postgres')
    password: str = Field('postgres')
    driver: str = Field('asyncpg')
    name: str

    @property
    def url(self) -> str:
        """Формирует строку подключения к PostgreSQL."""
        return f'postgresql+{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'
