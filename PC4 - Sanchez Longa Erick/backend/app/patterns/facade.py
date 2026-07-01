import random

class SearchFacade:
    @staticmethod
    def process_image_search(filename: str, search_type: str):
        # Simulamos un procesamiento complejo de IA
        mock_probability = round(random.uniform(70.0, 99.9), 1)
        
        return {
            "status": "success",
            "message": f"Imagen '{filename}' analizada correctamente.",
            "search_type": search_type,
            "results": [
                {
                    "match_percentage": f"{mock_probability}%",
                    "status_found": search_type,
                    "mock_note": "Este es un resultado simulado por el patrón Facade."
                }
            ]
        }