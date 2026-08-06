from typing import Annotated
from fastapi import Depends
from app.database.session import get_session
from app.services.api import ApiService
from app.services.monitor import MonitorService
from app.services.url import UrlService
from sqlalchemy.ext.asyncio import AsyncSession

SessionDep = Annotated[AsyncSession, Depends(get_session)]


def get_api_service(session: SessionDep) -> ApiService:
    return ApiService(session=session)


def get_monitor_service(session: SessionDep) -> MonitorService:
    return MonitorService(session=session)


def get_url_service(session: SessionDep) -> UrlService:
    return UrlService(session=session)


ApiServiceDep = Annotated[ApiService, Depends(get_api_service)]
UrlServiceDep = Annotated[UrlService, Depends(get_url_service)]
MonitorServiceDep = Annotated[MonitorService, Depends(get_monitor_service)]
