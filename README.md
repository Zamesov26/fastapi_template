# FastAPI Template

Базовый шаблон асинхронного API на FastAPI с PostgreSQL, миграциями Alembic и настроенными инструментами контроля качества.

## Технологии

- FastAPI и Uvicorn;
- SQLAlchemy 2.0 и asyncpg;
- Pydantic Settings;
- Alembic;
- pytest и HTTPX;
- Ruff и mypy.

## Быстрый старт

Требования: Python 3.12+ и PostgreSQL.

```bash
git clone <repository-url>
cd fastapi_template

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install -r dev.requirements.txt

cp .example.env .env
```

Для активации виртуального окружения в Windows:

```powershell
.venv\Scripts\activate
```

Укажите параметры подключения к PostgreSQL в `.env`. Обязательный параметр — `DB_NAME`.

## Запуск

Сервер разработки с автоматической перезагрузкой:

```bash
python dev_run.py
```

Или напрямую через Uvicorn:

```bash
uvicorn src.main:create_app --factory --reload --host 0.0.0.0 --port 8000
```

После запуска доступны:

- API: `http://localhost:8000`;
- Swagger UI: `http://localhost:8000/docs`;
- ReDoc: `http://localhost:8000/redoc`;
- liveness: `GET /api/v1/health/live`;
- readiness с проверкой PostgreSQL: `GET /api/v1/health/ready`.

## Команды разработки

```bash
make test          # Запустить тесты
make lint          # Проверить код с помощью Ruff
make format-check  # Проверить форматирование
make format        # Отформатировать код
make typecheck     # Проверить типы с помощью mypy
```

Дополнительные команды автоматического исправления доступны в `Makefile`.

## Docker

Docker Compose запускает только API и не создаёт PostgreSQL. Параметры внешней
базы данных передаются контейнеру из корневого `.env`.

Если PostgreSQL запущен на машине разработчика, укажите:

```dotenv
DB_HOST=host.docker.internal
```

Сборка и запуск API:

```bash
make docker-up
```

Применение миграций и просмотр логов:

```bash
make docker-migrate
make docker-logs
```

Остановка контейнера:

```bash
make docker-down
```

## Миграции

Создать миграцию:

```bash
alembic revision --autogenerate -m "описание изменений"
```

Применить миграции:

```bash
alembic upgrade head
```

Проверить текущее состояние:

```bash
alembic current
```

## Конфигурация

Настройки загружаются из переменных окружения и корневого файла `.env`. Путь к
файлу определяется относительно проекта и не зависит от текущей рабочей
директории.

Переменные окружения имеют приоритет над значениями из `.env`. В Docker Compose
следует передавать их контейнеру через `env_file` или `environment`; код
приложения при этом не зависит от расположения каталога `infra`.

| Переменная | Описание | Значение по умолчанию |
|---|---|---|
| `API_NAME` | Название приложения | `Application name API` |
| `API_DEBUG` | Режим отладки | `False` |
| `API_VERSION` | Версия API | `0.1.0` |
| `DB_HOST` | Адрес PostgreSQL | `localhost` |
| `DB_PORT` | Порт PostgreSQL | `5432` |
| `DB_USER` | Пользователь PostgreSQL | `postgres` |
| `DB_PASSWORD` | Пароль PostgreSQL | `postgres` |
| `DB_NAME` | Имя базы данных | обязательный параметр |
| `DB_DRIVER` | Драйвер SQLAlchemy | `asyncpg` |

Для интеграционных тестов используются аналогичные переменные с префиксом
`TEST_DB_`. По умолчанию тесты подключаются к базе `test_db` на `localhost`.

Пример значений находится в `.example.env`. Файл `.env` исключён из Git.

## Структура проекта

```text
fastapi_template/
├── src/
│   ├── api/          # Сборка маршрутов HTTP API
│   ├── database/     # Настройки БД и миграции
│   ├── domains/      # Домены, модели, схемы и бизнес-логика
│   ├── web/          # Общая веб-инфраструктура и middleware
│   ├── config.py     # Общие правила загрузки окружения
│   ├── main.py
│   └── settings.py
├── tests/            # Тесты и фикстуры
├── infra/            # Dockerfile и Docker Compose
├── .github/workflows/ # CI-проверки
├── alembic.ini
├── dev_run.py
├── Makefile
└── pyproject.toml
```

Каждый домен размещается в `src/domains/` и содержит собственные модели, схемы,
сервисы и HTTP router. Доменные routers подключаются в `src/api/router.py`,
модели регистрируются в `src/database/model_registry.py`, а глобальные
middleware — в `src/web/middlewares/setup.py`.

Код разделяется по ответственности:

- `domains` хранит предметную логику, модели, схемы и доменные routers;
- `database` хранит общие компоненты SQLAlchemy, миграции и зависимость сессии;
- `api` собирает routers доменов в общий API;
- `web` хранит middleware и другую общую HTTP-инфраструктуру.

При добавлении домена с SQLAlchemy-моделями путь к его модулю нужно
добавить в `MODEL_MODULES` в `src/database/model_registry.py`.

Имена индексов и ограничений формируются по общему naming convention из
`src/database/base.py`, поэтому миграции Alembic получают стабильные имена
объектов схемы.

При push и pull request GitHub Actions запускает lint, проверку
форматирования, typecheck и тесты.
