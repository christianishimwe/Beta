
from app.api.schemas.api import ApiCreate
from app.database.models import Apis
from app.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession


class ApiService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Apis, session=session)

    async def add(self, api: ApiCreate):
        api_entry = Apis(**api.model_dump())
        new_api = await self._add(api_entry)
        return new_api
