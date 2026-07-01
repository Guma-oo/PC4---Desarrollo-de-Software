from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Caregiver
from app.schemas import CaregiverCreate, CaregiverResponse

router = APIRouter()

@router.post("/", response_model=CaregiverResponse)
def create_caregiver(caregiver: CaregiverCreate, db: Session = Depends(get_db)):
    db_cg = Caregiver(**caregiver.dict())
    db.add(db_cg)
    db.commit()
    db.refresh(db_cg)
    return db_cg

@router.get("/", response_model=list[CaregiverResponse])
def get_caregivers(db: Session = Depends(get_db)):
    return db.query(Caregiver).all()