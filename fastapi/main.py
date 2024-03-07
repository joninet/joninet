from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette.responses import HTMLResponse
import sqlite3

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return open("static/index.html").read()

@app.get("/Actualizado", response_class=HTMLResponse)
def index():
    return open("static/datosActualizados.html").read()

@app.delete("/productos/{producto_id}")
def delete_producto(producto_id: int):
    conn = sqlite3.connect('base_datos.db')
    cursor = conn.cursor()

    # Convertir el parámetro a una cadena
    producto_id_str = str(producto_id)

    # Eliminar el producto con el ID proporcionado
    cursor.execute("DELETE FROM Producto WHERE id = ?", (producto_id_str,))
    conn.commit()

    return {"mensaje": "Producto eliminado correctamente"}