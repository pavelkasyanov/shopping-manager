from fastapi import APIRouter

from .user_handlers import router as user_router

api_router = APIRouter(prefix="/api")

api_router.include_router(user_router, tags=["users"])
