"""Настройки подключения к базе данных."""

from pydantic import Field
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL

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
        return URL.create(
            drivername=f'postgresql+{self.driver}',
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name,
        ).render_as_string(hide_password=False)
