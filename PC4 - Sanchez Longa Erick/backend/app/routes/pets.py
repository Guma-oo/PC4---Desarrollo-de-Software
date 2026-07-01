from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import PetCreate, PetResponse
from app.services.pet_service import PetService

router = APIRouter()

@router.post("/", response_model=PetResponse)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    return PetService.create_pet(db, pet)

@router.get("/", response_model=list[PetResponse])
def get_pets(db: Session = Depends(get_db), sort_by: str = Query(None)):
    return PetService.get_all_pets(db, sort_by)

@router.put("/{pet_id}/advance-status", response_model=PetResponse)
def advance_status(pet_id: int, db: Session = Depends(get_db)):
    return PetService.advance_pet_status(db, pet_id)