"""Запуск локального сервера разработки."""

import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        host='0.0.0.0',  # noqa: S104 — доступ из Docker и локальной сети.
        port=8000,
        reload=True,
    )
