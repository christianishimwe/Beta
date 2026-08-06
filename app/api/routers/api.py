
from fastapi import APIRouter

from app.api.schemas import api

router = APIRouter(tags=["API"], prefix="/api")


@router.post("/")
async def submit_api(api: api.BaseApi):
    pass
