# Hacer lo siguiente en la terminal, antes que nada:
 
# PS C:\Users\Jesy\Desktop\Modelado_Software> python -m venv env
# PS C:\Users\Jesy\Desktop\Modelado_Software> .\env\Scripts\activate
# (env) PS C:\Users\Jesy\Desktop\Modelado_Software> pip install fastapi uvicornv


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

# Crear un nuevo mensaje
@app.post("/mensajes", response_model=Mensaje)
def crear_mensaje(mensaje: Mensaje):
    mensaje.id = len(mensajes_db) + 1
    mensajes_db.append(mensaje)
    return mensaje

# Obtener un mensaje por su ID
@app.get("/mensajes/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensajes_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

# Listar todos los mensajes
@app.get("/mensajes", response_model=List[Mensaje])
def listar_mensajes():
    return mensajes_db

# Actualizar un mensaje existente
@app.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id: int, mensaje_actualizado: Mensaje):
    for index, mensaje in enumerate(mensajes_db):
        if mensaje.id == mensaje_id:
            mensaje_actualizado.id = mensaje_id
            mensajes_db[index] = mensaje_actualizado
            return mensaje_actualizado
    raise HTTPException(status_code=404, detail="Mensaje no encontrado para actualizar")

# Eliminar un mensaje por su ID
@app.delete("/mensajes/{mensaje_id}", response_model=dict)
def eliminar_mensaje(mensaje_id: int):
    for index, mensaje in enumerate(mensajes_db):
        if mensaje.id == mensaje_id:
            del mensajes_db[index]
            return {"detail": "Mensaje eliminado"}
    raise HTTPException(status_code=404, detail="Mensaje no encontrado para eliminar")

 
"""
En la terminal, ejecutar:

uvicorn main:app --reload
Abrí el navegador en:

http://localhost:8000 para ver la bienvenida 

http://localhost:8000/docs para usar el panel interactivo de Fast

PARA INTERACTUAR EN FASTAPI:

Busca el endpoint que se quiere probar, por ejemplo POST /mensajes

Clic en la flechita del título para expandirlo

Clic en "Try it out" (que está arriba a la derecha dentro del cuadro expandido, y sirve 
para desbloquear el campo, para poder editarlo)

El campo JSON aparecerá editable (ya no gris o bloqueado)

Escribir el JSON (por ejemplo): "user": "Juan", "mensaje": "¡Hola a todos!". 
IMPORTANTE: NO ESCRIBIR NADA EN CODIGO, PORQUE DE TODAS MANERAS POR EL ALGORITMO SE VA 
            IGNORAR.

Haz clic en "Execute"

En la parte de abajo se mostrará la respuesta que devuelve el servidor 
con el mensaje creado (y el id asignado).

PARA CREAR OTRO MENSAJE: "CLEAR" Y DESPUES DE NUEVO "Try it out"

Para ver todos los mensajes: GET /mensajes listar mensajes, try in out, execute
#_______________________________________________________________________________________________________________

EXPLICACION DEL CODIGO

from typing import Optional, List
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, HTTPException


#from typing import Optional, List

#Este módulo (typing) contiene herramientas para declarar tipos de datos de manera más precisa.
#  Se usa especialmente con Pydantic y FastAPI para indicar qué tipo de datos esperamos.

# Optional: significa que un valor puede ser del tipo indicado o puede ser None (nulo)
#      Ejemplo: Optional[str] significa que el campo puede ser una cadena de texto o None.

# List: permite especificar que un campo es una lista de elementos de un cierto tipo.
#        Ejemplo: List[int] es una lista de enteros como [1, 2, 3].

#_____________________________________________________________________________________________________

#from pydantic import BaseModel, EmailStr

# Pydantic es una biblioteca que permite crear modelos de datos en Python y validarlos automáticamente.
# BaseModel: se usa como clase base para definir nuestros propios modelos de datos.
# Al heredar de BaseModel, creas una clase que puede validar automáticamente los datos 
#           (por ejemplo, asegurarse de que un campo sea entero o correo válido).
# EmailStr: un tipo especial de campo que valida que el valor ingresado sea un correo electrónico válido.

#_____________________________________________________________________________________________________

#from fastapi import FastAPI, HTTPException

# FastAPI es el framework para construir la API.
# FastAPI: es la clase principal para crear la aplicación. 
#      Se instancia como app = FastAPI() y se usa para declarar rutas y lógica.
# HTTPException: se usa para lanzar errores HTTP personalizados, 
#      como por ejemplo devolver un error 404 si no se encuentra un usuario.

#  ¿Qué es HTTP?
# HTTP es el protocolo que usan los navegadores y servidores web para comunicarse. 
# Cada vez que visitas una página web o haces una solicitud en una API,
#  se devuelve un código de estado HTTP que indica cómo fue la operación.

# ¡Qué significa el 404?
# Un error 404 es un código de estado HTTP que significa:"Recurso no encontrado".

# ¿Por qué se llama 404?
# El número 404 es parte de una serie de códigos que siguen esta estructura:
#         [Clase del error][Código específico]
# En este caso: 4 → indica un error del cliente (es decir, el problema no está en el servidor,
#                    sino en la solicitud que hizo el usuario).
#               04 restante → indica “No encontrado” (“Not Found”).

¿Qué es un endpoint?

Es una dirección URL específica en la API donde se puede acceder a cierta funcionalidad o recurso.

Es como una puerta o un punto de contacto para que un cliente (como una app o navegador) pida o mande
 información.

"""
