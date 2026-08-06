from fastapi import APIRouter


router = APIRouter(tags=["Monitors"], prefix="/monitors")


@router.get("/")
async def submit_monitor():
    return {"monitors successfull submittted"}
