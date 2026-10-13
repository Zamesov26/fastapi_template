"""Проверять явную регистрацию доменных моделей."""

from src.database import model_registry


class TestModelRegistry:
    """Проверять импорт перечисленных модулей моделей."""

    def test_imports_every_registered_module(self, monkeypatch):
        """Импортировать каждый модуль из реестра в заданном порядке."""
        imported_modules: list[str] = []
        monkeypatch.setattr(
            model_registry,
            'MODEL_MODULES',
            ('src.domains.users.models', 'src.domains.orders.models'),
        )
        monkeypatch.setattr(model_registry, 'import_module', imported_modules.append)

        model_registry.register_models()

        assert imported_modules == [
            'src.domains.users.models',
            'src.domains.orders.models',
        ]
