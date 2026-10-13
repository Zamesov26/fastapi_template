from pydantic import Field
from pydantic_settings import BaseSettings

from src.api.settings import APISettings
from src.database.settings import DBSettings


class Settings(BaseSettings):
    """Объединённые настройки приложения."""

    api: APISettings = Field(default_factory=APISettings)
    db: DBSettings = Field(default_factory=DBSettings)
