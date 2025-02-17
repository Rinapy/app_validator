# schemas.py
from pydantic import BaseModel

class AppInstanceCreate(BaseModel):
    title: str
    description: str

class AppInstance(AppInstanceCreate):
    id: int

    class Config:
        orm_mode = True