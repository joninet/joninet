# ingreos_app/main.py
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime
import sqlite3

app = FastAPI()

# Configuración para usar templates HTML
templates = Jinja2Templates(directory="templates")


# Ruta principal que renderiza el formulario
@app.get("/", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("ingreso_form.html", {"request": request})


# Ruta para procesar el formulario y guardar en la base de datos
@app.post("/registrar_ingreso/")
async def registrar_ingreso(
    codigo: str = Form(...),
    nombre: str = Form(...),
    cantidad: int = Form(...),
):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Conexión a la base de datos SQLite
    conn = sqlite3.connect("ingresos.db")
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

    # Insertar datos en la tabla
    cursor.execute(
        """
        INSERT INTO ingresos (codigo, nombre, cantidad, fecha)
        VALUES (?, ?, ?, ?)
        """,
        (codigo, nombre, cantidad, fecha_actual),
    )

    # Commit y cerrar la conexión
    conn.commit()
    conn.close()

    return {"mensaje": "Ingreso registrado con éxito"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
