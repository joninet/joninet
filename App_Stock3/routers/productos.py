from fastapi import APIRouter, HTTPException, Query, Path
from helpers.funciones_db import FuncionesDB

router = APIRouter()

@router.post('/productos/{nombre}/{um}/{descripcion}/{categoria_id}')
async def crearProducto(
    nombre: str = Path(..., title="Nombre del producto"),
    um: str = Path(..., title="Unidad de Medida del producto"),
    descripcion: str = Path(..., title="descripcion del producto"),
    categoria_id: int = Path(..., title="id de la categoria del producto")):

    column = ["nombre", "um", "descripcion", "categoria_id"]
    values = [nombre, um, descripcion, categoria_id]

    insertar = FuncionesDB()
    insertar.insertarDatos("Producto", column, values)
    return {"message": "Ingreso Correcto"}