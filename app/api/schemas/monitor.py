from pydantic import BaseModel


class BaseMonitor(BaseModel):
    url_id: str
    interval: float
    is_active: bool
