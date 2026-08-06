
from fastapi import APIRouter, status

from app.api.dependencies import ApiServiceDep
from app.api.schemas import api
from app.services.api import ApiService

router = APIRouter(tags=["API"], prefix="/api")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def submit_api(api: api.ApiCreate, service: ApiServiceDep):
    new_api = await service.add(api)
    return new_api
