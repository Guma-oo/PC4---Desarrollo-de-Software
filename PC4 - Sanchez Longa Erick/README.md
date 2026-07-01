#Sistema de Búsqueda de Mascotas

Utilice una arquitectura por capas: **Backend (API REST)** y **Frontend (Interfaz de Usuario)**.

* **Reporte de Mascotas Perdidas:** Registro dinámico de datos clave (nombre, especie, raza, descripción y ubicación) con actualización y visualización en tiempo real.
* **Ciclo de Vida(State):** Gestión del flujo de los reportes, permitiendo transicionar estados de forma controlada.
* **Buscador por Imagen Inteligente (Facade):** Simulación de un sistema avanzado de reconocimiento visual para clasificar mascotas en adopción, venta o verificación de pérdida.
* **Gestión de Cuidadores y Alertas (Observer):** Registro de cuidadores solidarios o profesionales que reciben alertas automáticas inmediatas cuando una nueva mascota es reportada.
* **Ordenamiento Flexible (Strategy):** Filtros avanzados en el frontend para organizar las listas dinámicamente según diferentes criterios de negocio.

---

## Estructura del Proyecto

El software implementa una **arquitectura por capas** en el backend para aislar responsabilidades de forma clara y entendible:

```text
project/
├── backend/                # Capa del Servidor (API REST)
│   ├── app/
│   │   ├── main.py        # Inicialización de FastAPI y Middlewares
│   │   ├── database.py    # Configuración de conexiones
│   │   ├── models.py      # Estructura de tablas del ORM (SQLAlchemy)
│   │   ├── schemas.py     # Validadores y Tipado de Datos (Pydantic)
│   │   ├── patterns/      # Módulo exclusivo de Patrones de Diseño
│   │   ├── routes/        # Controladores y Endpoints HTTP
│   │   └── services/      # Capa de Lógica de Negocio Centralizada
│   └── requirements.txt
└── frontend/               # Capa de Cliente (Interfaz Web limpia)
    ├── css/               # Estilos personalizados
    ├── js/                # Scripts asíncronos (Fetch API)
    ├── assets/            # Recursos estáticos e imágenes de prueba
    ├── index.html
    ├── pets.html
    ├── caregivers.html
    └── search.html
