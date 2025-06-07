from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

# Modelo del mensaje
class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str

# Crear instancia de la aplicación FastAPI
app = FastAPI()

# Base de datos simulada (lista en memoria)
mensajes_db: List[Mensaje] = []

# Ruta de bienvenida
@app.get("/")
def inicio():
    return { "mensaje": "🍽️ Bienvenidos a 'LA CUCHARA REBELDE' - COCINA FACIL Y ENTRETENIDA 😋😋😋",
        "endpoints_disponibles": ["/mensajes", "/mensajes/{id}"]}
