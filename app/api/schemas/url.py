from uuid import UUID
from pydantic import BaseModel


class BaseUrl(BaseModel):
    url: str
    api_id: UUID
