"""Обработчики проверки доступности приложения."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.dependencies import get_session

router = APIRouter()


@router.get('/health/live')
async def liveness() -> dict[str, str]:
    """Подтвердить, что процесс приложения обрабатывает запросы."""
    return {'status': 'alive'}


@router.get('/health/ready')
async def readiness(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> dict[str, str]:
    """Подтвердить готовность приложения и доступность базы данных."""
    try:
        await session.execute(select(1))
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Database is unavailable',
        ) from error

    return {'status': 'ready'}
