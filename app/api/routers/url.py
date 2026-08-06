from fastapi import APIRouter, status

from app.api.dependencies import UrlServiceDep
from app.api.schemas import url

router = APIRouter(tags=["URLs"], prefix="/urls")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def submit_url(url: url.UrlCreate, service: UrlServiceDep):
    new_url = await service.add(url)
    return new_url
