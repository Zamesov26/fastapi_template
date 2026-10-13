.PHONY: lint lint-preview lint-fix format format-check ruff-all typecheck test

# Показать все проблемы без изменения файлов.
lint:
	ruff check .

# Показать проблемы и доступные автоматические исправления.
lint-preview:
	ruff check . --show-fixes

# Автоматически исправить безопасные проблемы.
lint-fix:
	ruff check . --fix

# Проверить форматирование без изменения файлов.
format-check:
	ruff format . --check

# Отформатировать код.
format:
	ruff format .

# Применить форматирование и все доступные исправления.
ruff-all:
	ruff format .
	ruff check . --fix --unsafe-fixes

# Проверить статические типы Python-кода.
typecheck:
	mypy src tests dev_run.py

# Запустить тесты.
test:
	pytest
