from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """Вернуть состояние доступности сервиса."""
    return {"status": "healthy", "message": "FastAPI service is running"}
