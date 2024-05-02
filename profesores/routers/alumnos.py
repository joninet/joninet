from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse
from helpers.funciones_db import FuncionesDB
import sqlite3

router = APIRouter()

@router.post('/alumnos/crear')
async def crearAlumnos(
    req: Request,
    nombres: str = Form(None),
    apellidos: str = Form(None),
    email: str = Form(None),
    id_colegio: int = Form(None)):

    nombres = nombres.upper()
    apellidos = apellidos.upper()


    column = ["nombres", "apellidos", "email", "id_colegio"]
    values = [nombres, apellidos, email, id_colegio]

    insertar = FuncionesDB()
    insertar.insertarDatos("alumnos", column, values)

    return {"message": "creado"}

@router.post('/alumnos/borrar/{alumnos_id}')
def borarGrados(alumnos_id: int):
    ver = FuncionesDB()
    ver.borrarRegistro("alumnos", alumnos_id)

    return {"message": "Registro borrado correctamente"}