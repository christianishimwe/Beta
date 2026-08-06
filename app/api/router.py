

from fastapi import APIRouter

from app.api.routers import api, monitors


master_router = APIRouter()
master_router.include_router(monitors.router)
master_router.include_router(api.router)
