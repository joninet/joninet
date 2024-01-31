from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime
import sqlite3

# Clase Producto

class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

# Clase Ingreso

class Ingreso(Producto):
    def __init__(self, codigo, nombre, cantidad):
        super().__init__(codigo, nombre)
        self.cantidad = cantidad

# Instancia de la API

app = FastAPI()

# Plantilla HTML

templates = Jinja2Templates(directory="templates")

# Rutas de la API

@app.get("/")
def index(request: Request):  # Inject the request object
    return templates.TemplateResponse("index.html", {"request": request, "now": datetime.now()})

@app.post("/ingresar")
def ingresar(codigo: str, nombre: str, cantidad: int):
    ingreso = Ingreso(codigo, nombre, cantidad)
    ingreso.guardar()
    return HTMLResponse(content="Ingreso registrado")

# Función para guardar el ingreso

def guardar(ingreso):
    # Conectar a la base de datos
    conexion = sqlite3.connect("ingresos.db")

    # Crear el cursor
    cursor = conexion.cursor()

    # Insertar el registro
    cursor.execute("INSERT INTO ingresos (codigo, nombre, cantidad, fecha) VALUES (?, ?, ?, ?)", (ingreso.codigo, ingreso.nombre, ingreso.cantidad, datetime.now()))

    # Cerrar la conexión
    conexion.commit()
    conexion.close()
