# API REST - MENSAJES

## Descripción

Esta API está desarrollada con **FastAPI** y permite gestionar mensajes simples en memoria. Es un servicio básico para crear, leer, actualizar y eliminar mensajes que contienen un usuario y un texto.

---

## Funcionalidades

- **Crear mensajes:** Permite agregar un nuevo mensaje con un usuario y texto.
- **Listar mensajes:** Devuelve todos los mensajes almacenados.
- **Obtener mensaje por ID:** Consulta un mensaje específico usando su identificador.
- **Actualizar mensajes:** Modifica el contenido de un mensaje existente por su ID.
- **Eliminar mensajes:** Borra un mensaje por su ID.

Todos los mensajes se almacenan en una lista en memoria (no usa base de datos externa).

---

## Endpoints disponibles

| Método | Ruta               | Descripción                        |
|--------|--------------------|----------------------------------|
| GET    | `/`                | Mensaje de bienvenida y endpoints disponibles |
| GET    | `/mensajes`        | Lista todos los mensajes          |
| GET    | `/mensajes/{id}`   | Obtiene un mensaje por ID         |
| POST   | `/mensajes`        | Crea un nuevo mensaje             |
| PUT    | `/mensajes/{id}`   | Actualiza un mensaje existente    |
| DELETE | `/mensajes/{id}`   | Elimina un mensaje por ID         |

---

## Modelo de datos

Cada mensaje tiene la siguiente estructura:

```json
{
  "id": 1,
  "user": "nombre_usuario",
  "mensaje": "texto del mensaje"
}
