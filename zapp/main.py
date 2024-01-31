# main.py

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import datetime
import sqlite3

app = FastAPI()

# Conectar a la base de datos SQLite
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS ingresos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT,
        nombre TEXT,
        cantidad INTEGER,
        fecha TEXT
    )
    """
)
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()

# Definir las clases para los modelos
class Producto:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre


class Ingreso(Producto):
    def __init__(self, codigo: str, nombre: str, cantidad: int):
        super().__init__(codigo, nombre)
        self.cantidad = cantidad


# Definir el modelo Pydantic para la validación del formulario
class IngresoForm(BaseModel):
    codigo: str
    nombre: str
    cantidad: int


# Configurar el sistema de plantillas Jinja2
templates = Jinja2Templates(directory="templates")


# Definir las rutas
@app.post("/registrar_ingreso/")
async def registrar_ingreso(request: Request, ingreso_form: IngresoForm = Form(...)):
    ingreso = Ingreso(
        codigo=ingreso_form.codigo,
        nombre=ingreso_form.nombre,
        cantidad=ingreso_form.cantidad,
    )

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Insertar el ingreso en la base de datos
    cursor.execute(
        "INSERT INTO ingresos (codigo, nombre, cantidad, fecha) VALUES (?, ?, ?, ?)",
        (ingreso.codigo, ingreso.nombre, ingreso.cantidad, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    )
    conn.commit()

    # Cerrar la conexión a la base de datos
    conn.close()

    return templates.TemplateResponse(
        "registro_exitoso.html",
        {"request": request, "ingreso": ingreso},
    )


@app.get("/")
async def mostrar_formulario(request: Request):
    return templates.TemplateResponse("formulario_ingreso.html", {"request": request})
