import httpx
import time


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
