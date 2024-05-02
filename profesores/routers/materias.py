from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse
from helpers.funciones_db import FuncionesDB
import sqlite3

router = APIRouter()

@router.post('/materias/crear')
async def crearMaterias(
    req: Request,
    nombre: str = Form(None),
    id_colegio: int = Form(None),
    id_grado: int = Form(None)):

    column = ["nombre", "id_colegio", "id_grado"]
    values = [nombre, id_colegio, id_grado]

    insertar = FuncionesDB()
    insertar.insertarDatos("materias", column, values)

    return {"message": "creado"}

@router.post('/materias/borrar/{materias_id}')
def borarGrados(materias_id: int):
    ver = FuncionesDB()
    ver.borrarRegistro("materias", materias_id)

    return {"message": "Registro borrado correctamente"}