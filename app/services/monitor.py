from app.api.schemas.monitor import MonitorCreate
from app.database.models import Monitors
from app.services.base import BaseService


class MonitorService(BaseService):
    def __init__(self, session):
        super().__init__(model=Monitors, session=session)

    def add_monitor(self, monitor: MonitorCreate):
        monitor_entry = Monitors(**monitor.model_dump())
        new_monitor = self._add(monitor_entry)
        return new_monitor
