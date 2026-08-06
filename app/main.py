
from fastapi import FastAPI
from app.api.router import master_router

app = FastAPI()

app.include_router(master_router)
