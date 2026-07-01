from pydantic import BaseModel
from typing import Optional, List

class PetCreate(BaseModel):
    name: str
    species: str
    breed: str
    description: str
    location: str
    photo_url: Optional[str] = None

class PetResponse(PetCreate):
    id: int
    status: str # <--- LÍNEA NUEVA
    class Config:
        from_attributes = True

class CaregiverCreate(BaseModel):
    name: str
    caregiver_type: str
    accepted_species: str
    alerts_active: bool = True

class CaregiverResponse(CaregiverCreate):
    id: int
    class Config:
        from_attributes = True