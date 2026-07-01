from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.patterns.singleton import Base

class PetReport(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String)
    breed = Column(String)
    description = Column(String)
    location = Column(String)
    photo_url = Column(String, nullable=True)
    status = Column(String, default="Perdida") # <--- LÍNEA NUEVA

class Caregiver(Base):
    __tablename__ = "caregivers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    caregiver_type = Column(String) # Solidario, Profesional, Especializado
    accepted_species = Column(String)
    alerts_active = Column(Boolean, default=True)
    notifications = relationship("Notification", back_populates="caregiver")

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    caregiver_id = Column(Integer, ForeignKey("caregivers.id"))
    message = Column(String)
    
    caregiver = relationship("Caregiver", back_populates="notifications")