from fastapi import APIRouter, status

from app.api.dependencies import MonitorServiceDep
from app.api.schemas import monitor

router = APIRouter(tags=["Monitors"], prefix="/monitors")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_monitor(monitor: monitor.MonitorCreate, service: MonitorServiceDep):
    new_monitor = await service.add_monitor(monitor)
    return new_monitor
