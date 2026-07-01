from app.patterns.singleton import db_singleton, Base

# Exponemos get_db para las dependencias de FastAPI
get_db = db_singleton.get_db