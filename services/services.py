# services.py
from sqlalchemy.orm import Session
from domain.database import Task
from domain.schemas import AppInstance

class AppInstanceService:
    @staticmethod
    def create_app_instance(db: Session, app_instance: AppInstance):
        db_app_instance = AppInstance(title=app_instance.title, description=app_instance.description)
        db.add(db_app_instance)
        db.commit()
        db.refresh(db_app_instance)
        return db_app_instance

    @staticmethod
    def update_app_instance(db: Session, app_instance: AppInstance):
        db.query(AppInstance).filter(AppInstance.id == app_instance.id).update(app_instance.model_dump())
        db.commit()
        db.refresh(app_instance)
        return app_instance

    @staticmethod
    def get_task(db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()