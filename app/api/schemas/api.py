from pydantic import BaseModel


class BaseApi(BaseModel):
    name: str


class ApiCreate(BaseApi):
    pass
