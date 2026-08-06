

from fastapi import APIRouter

from app.api.routers import api, monitors, url


master_router = APIRouter()
master_router.include_router(monitors.router)
master_router.include_router(api.router)
master_router.include_router(url.router)
