from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse
from helpers.funciones_db import FuncionesDB
import sqlite3

router = APIRouter()

@router.post('/grados/crear')
async def crearGrados(
    req: Request,
    nombre: str = Form(None),
    division: str = Form(None)):

    division = division.upper()

    column = ["nombre", "division"]
    values = [nombre, division]

    insertar = FuncionesDB()
    insertar.insertarDatos("grados", column, values)

    return {"message": "creado"}

@router.post('/grados/borrar/{grados_id}')
def borarGrados(grados_id: int):
    ver = FuncionesDB()
    ver.borrarRegistro("grados", grados_id)

    return {"message": "Registro borrado correctamente"}