from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse
from helpers.funciones_db import FuncionesDB
import sqlite3

router = APIRouter()

@router.post('/colegio/crear')
async def crearColegio(
    req: Request,
    nombre: str = Form(None)):

    column = ["nombre"]
    values = [nombre]

    insertar = FuncionesDB()
    insertar.insertarDatos("colegios", column, values)

    return {"message": "creado"}

@router.post('/colegio/borrar/{colegio_id}')
def borarColegio(colegio_id: int):
    ver = FuncionesDB()
    ver.borrarRegistro("colegios", colegio_id)

    return {"message": "Registro borrado correctamente"}