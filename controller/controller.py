from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.database import SessionLocal, engine, Base
from domain.schemas import AppInstanceCreate, AppInstance
from services.services import AppInstanceService

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/appinstances/", response_model=AppInstance)
def create_app_instance(app_instance: AppInstanceCreate, db: Session = Depends(get_db)):
    return AppInstanceService.create_app_instance(db, app_instance)

@app.get("/appinstances/", response_model=list[AppInstance])
def read_app_instances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return AppInstanceService.get_app_instances(db, skip=skip, limit=limit)

@app.get("/appinstances/{app_instance_id}", response_model=AppInstance)
def read_app_instance(app_instance_id: int, db: Session = Depends(get_db)):
    db_app_instance = AppInstanceService.get_app_instance(db, app_instance_id)
    if db_app_instance is None:
        raise HTTPException(status_code=404, detail="AppInstance not found")
    return db_app_instance