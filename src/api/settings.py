"""Настройки HTTP API."""

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from src.config import AppBaseSettings


class APISettings(AppBaseSettings):
    """Настройки HTTP API приложения."""

    model_config = SettingsConfigDict(env_prefix='API_')

    name: str = Field('Application name API')
    debug: bool = Field(False)
    version: str = Field('0.1.0')
