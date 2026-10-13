"""Реестр моделей SQLAlchemy для автогенерации миграций.

Пути к модулям моделей доменов явно перечисляются в ``MODEL_MODULES``.
Их импорт регистрирует таблицы в ``Base.metadata`` до запуска Alembic.
"""

from importlib import import_module

MODEL_MODULES: tuple[str, ...] = ()


def register_models() -> None:
    """Импортировать все модули с доменными моделями."""
    for module_path in MODEL_MODULES:
        import_module(module_path)
