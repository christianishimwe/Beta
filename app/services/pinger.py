import httpx
import time
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import col
from app.database.models import Monitors


async def ping(url: str):
    start = time.monotonic()
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=url,
                timeout=5.0
            )
        return {
            "status_code": response.status_code,
            "response_ms": round((time.monotonic() - start) * 1000)
        }

    except httpx.TimeoutException:
        return {
            "status_code": None,
            "response_ms": round((time.monotonic() - start) * 1000)
        }


async def get_due_monitors(session: AsyncSession):
    # get all monitors that are active and due for a ping
    utc_now = func.timezone("UTC", func.now())
    query = select(Monitors).where(
        col(Monitors.is_active).is_(True),
        func.extract("epoch", utc_now -
                     col(Monitors.last_pinged_at)) >= Monitors.interval
    )

    result = await session.execute(query)
    return result.scalars().all()
