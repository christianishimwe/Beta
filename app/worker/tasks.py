import asyncio
from traceback import print_exception
from celery import Celery
from app.config import redis_settings
from app.services.pinger import ping

ping_url = "https://httpbin.org/status/200"
app = Celery(
    "beta_tasks",
    broker=redis_settings.REDIS_URL
)

app.conf.beat_schedule = {
    "ping_every_minute": {
        "task": "app.worker.tasks.run_pings",
        "schedule": 10.0,
        "args": (ping_url,)
    }
}


@app.task(name="app.worker.tasks.run_pings")
def run_pings(ping_url):
    result = asyncio.run(ping(ping_url))
    print(result)
