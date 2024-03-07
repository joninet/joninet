from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.post("/productos/{producto_id}")
def delete_producto(producto_id: int):
    conn = sqlite3.connect('base_datos.db')
    cursor = conn.cursor()

    # Eliminar el producto con el ID proporcionado
    cursor.execute("DELETE FROM Producto WHERE id = ?", (producto_id,))
    conn.commit()

    return {"mensaje": "Producto eliminado correctamente"}
