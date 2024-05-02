from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse
from helpers.funciones_db import FuncionesDB
import sqlite3

router = APIRouter()

@router.post('/parciales/crear')
async def crearParciales(
    req: Request,
    tema: str = Form(None),
    id_materia: int = Form(None),
    id_colegio: int = Form(None)):

    tema = tema.upper()

    column = ["tema", "id_materia", "id_colegio"]
    values = [tema, id_materia, id_colegio]

    insertar = FuncionesDB()
    insertar.insertarDatos("parciales", column, values)

    return {"message": "creado"}

@router.post('/parciales/borrar/{parciales_id}')
def borarGrados(parciales_id: int):
    ver = FuncionesDB()
    ver.borrarRegistro("parciales", parciales_id)

    return {"message": "Registro borrado correctamente"}