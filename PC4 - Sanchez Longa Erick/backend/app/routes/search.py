from fastapi import APIRouter, UploadFile, File, Form
from app.patterns.facade import SearchFacade

router = APIRouter()

@router.post("/")
def search_pet_image(
    file: UploadFile = File(...),
    search_type: str = Form(...) # Adopción, Venta, Verificar Pérdida
):
    # Usamos el patrón Facade para procesar la búsqueda mock
    result = SearchFacade.process_image_search(file.filename, search_type)
    return result