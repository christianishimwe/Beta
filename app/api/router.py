

from fastapi import APIRouter

from app.api.routers import monitors


master_router = APIRouter()
master_router.include_router(monitors.router)
