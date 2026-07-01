# Sistema de Búsqueda de Mascotas

Proyecto universitario simple, modular y funcional desarrollado con FastAPI y JS Vanilla.

## Estructura de Patrones de Diseño

El código demuestra la implementación de 3 patrones fundamentales (ubicados en `backend/app/patterns/`):

1. **Singleton (`singleton.py`)**: 
   - *Dónde se usa:* En la conexión con la base de datos SQLite.
   - *Por qué:* Garantiza que se utilice una única instancia del motor y la fábrica de sesiones de SQLAlchemy en toda la ejecución, evitando fugas de memoria por múltiples conexiones redundantes.
2. **Observer (`observer.py`)**: 
   - *Dónde se usa:* En el registro de nuevas mascotas perdidas (`routes/pets.py`).
   - *Por qué:* Desacopla la lógica. Cuando una mascota es reportada (Sujeto), notifica a los cuidadores (Observadores) que tienen `alerts_active` generando un registro de notificación, sin que el módulo de mascotas interactúe directamente con el de cuidadores.
3. **Facade (`facade.py`)**: 
   - *Dónde se usa:* En el endpoint de búsqueda por imagen (`routes/search.py`).
   - *Por qué:* Oculta la "complejidad" de un supuesto análisis de inteligencia artificial. El controlador solo llama a un método, y el Facade se encarga de estructurar y retornar la respuesta *mockeada* según el tipo de búsqueda (Adopción, Venta, Pérdida).

## Instalación y Ejecución

### 1. Backend
1. Abre una terminal y ve a la carpeta `backend/`.
2. Crea un entorno virtual (opcional pero recomendado): `python -m venv venv`
3. Instala dependencias:
   ```bash
   pip install -r requirements.txt