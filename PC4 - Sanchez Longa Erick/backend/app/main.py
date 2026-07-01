from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.patterns.singleton import Base, db_singleton
from app.routes import pets, caregivers, search

# Crear base de datos
Base.metadata.create_all(bind=db_singleton._instance.engine)

app = FastAPI(title="Búsqueda de Mascotas API")

# CORS para permitir peticiones desde el frontend local (HTML)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registramos las rutas
app.include_router(pets.router, prefix="/pets", tags=["Pets"])
app.include_router(caregivers.router, prefix="/caregivers", tags=["Caregivers"])
app.include_router(search.router, prefix="/search", tags=["Search"])