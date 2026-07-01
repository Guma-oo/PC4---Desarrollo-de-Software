from sqlalchemy.orm import Session
from app.models import Caregiver, Notification

class PetAlertObserver:
    @staticmethod
    def notify(db: Session, pet_name: str, species: str):
        # Buscamos cuidadores con alertas activas
        caregivers = db.query(Caregiver).filter(Caregiver.alerts_active == True).all()
        for caregiver in caregivers:
            # Lógica simple: Si acepta todas o la especie coincide
            if "todas" in caregiver.accepted_species.lower() or species.lower() in caregiver.accepted_species.lower():
                notification = Notification(
                    caregiver_id=caregiver.id,
                    message=f"¡Alerta! Mascota perdida: {pet_name} (Especie: {species})"
                )
                db.add(notification)
        db.commit()