"""Общие правила загрузки конфигурации приложения."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / '.env'


class AppBaseSettings(BaseSettings):
    """Базовый класс настроек с привязкой к корневому файлу окружения."""

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding='utf-8',
        extra='ignore',
    )
