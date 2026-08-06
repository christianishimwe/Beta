import asyncio
from datetime import datetime
from celery import Celery
from app.config import redis_settings
from app.database.session import async_session
from app.services.pinger import ping, get_due_monitors

app = Celery(
    "beta_tasks",
    broker=redis_settings.REDIS_URL
)

app.conf.beat_schedule = {
    "ping_every_minute": {
        "task": "app.worker.tasks.run_pings",
        "schedule": 10.0,
    }
}


async def _ping_due_monitors():
    async with async_session() as session:
        due_monitors = await get_due_monitors(session)
        results = await asyncio.gather(
            *(ping(monitor.url_id) for monitor in due_monitors)
        )

        for monitor in due_monitors:
            monitor.last_pinged_at = datetime.utcnow()

        await session.commit()

        return list(zip(due_monitors, results))


@app.task(name="app.worker.tasks.run_pings")
def run_pings():
    for monitor, result in asyncio.run(_ping_due_monitors()):
        print(monitor.url_id, result)
