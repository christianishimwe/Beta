from app.api.schemas.url import UrlCreate
from app.database.models import Urls
from app.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession


class UrlService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Urls, session=session)

    async def add(self, url: UrlCreate):
        url_entry = Urls(**url.model_dump())
        new_url = await self._add(url_entry)
        return new_url
