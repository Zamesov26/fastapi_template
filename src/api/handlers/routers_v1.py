"""Маршруты первой версии HTTP API."""

from fastapi import APIRouter

from src.api.handlers import life_handler

api_router = APIRouter()
api_router.include_router(life_handler.router)
