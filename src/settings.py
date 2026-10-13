"""Корневая конфигурация приложения."""

from pydantic import BaseModel, Field

from src.api.settings import APISettings
from src.database.settings import DBSettings


class Settings(BaseModel):
    """Объединённые настройки приложения."""

    api: APISettings = Field(default_factory=APISettings)
    db: DBSettings = Field(default_factory=DBSettings)
