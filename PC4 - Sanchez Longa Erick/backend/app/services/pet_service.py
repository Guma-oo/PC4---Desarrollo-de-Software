from sqlalchemy.orm import Session
from app.models import PetReport
from app.schemas import PetCreate
from app.patterns.observer import PetAlertObserver
from app.patterns.state import PetStateContext
from app.patterns.strategy import PetSorter, SortByNameStrategy, SortBySpeciesStrategy

class PetService:
    @staticmethod
    def get_all_pets(db: Session, sort_by: str = None):
        pets = db.query(PetReport).all()
        if sort_by == "name":
            sorter = PetSorter(SortByNameStrategy())
            pets = sorter.execute_sort(pets)
        elif sort_by == "species":
            sorter = PetSorter(SortBySpeciesStrategy())
            pets = sorter.execute_sort(pets)
        return pets

    @staticmethod
    def create_pet(db: Session, pet_data: PetCreate):
        db_pet = PetReport(**pet_data.dict())
        db.add(db_pet)
        db.commit()
        db.refresh(db_pet)
        PetAlertObserver.notify(db, pet_data.name, pet_data.species)
        return db_pet

    @staticmethod
    def advance_pet_status(db: Session, pet_id: int):
        pet = db.query(PetReport).filter(PetReport.id == pet_id).first()
        if pet:
            context = PetStateContext(pet.status)
            pet.status = context.advance_state()
            db.commit()
            db.refresh(pet)
        return pet