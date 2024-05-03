from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse
from helpers.funciones_db import FuncionesDB
import sqlite3
from datetime import datetime

router = APIRouter()

@router.post('/notas/crear')
async def crearNotas(
    req: Request,
    fecha: str = Form(None),
    nota: float = Form(None),
    rec1: float = Form(None),
    rec2: float = Form(None),
    rec3: float = Form(None),
    id_alumno: int = Form(None),
    id_parcial: int = Form(None)):

    fecha_datetime = datetime.strptime(fecha, "%Y-%m-%d")

    column = ["fecha", "nota", "rec1", "rec2", "rec3", "id_alumno", "id_parcial"]
    values = [fecha_datetime, nota, rec1, rec2, rec3, id_alumno, id_parcial]

    insertar = FuncionesDB()
    insertar.insertarDatos("notas", column, values)

    return {"message": "creado"}

@router.post("/notas/editardb")
async def editarNotas(
    req: Request,
    id: int = Form(None),
    fecha: str = Form(None),
    nota: float = Form(None),
    rec1: float = Form(None),
    rec2: float = Form(None),
    rec3: float = Form(None),
    id_alumno: int = Form(None),
    id_parcial: int = Form(None)):

    fecha_datetime = datetime.strptime(fecha, "%Y-%m-%d")

    column = ["fecha", "nota", "rec1", "rec2", "rec3", "id_alumno", "id_parcial"]
    values = [fecha_datetime, nota, rec1, rec2, rec3, id_alumno, id_parcial]

    editar = FuncionesDB()
    editar.editarRegistro("notas", column, values, f"id = ?", (id,))
    
    return {"message": "editado correctamente"}

@router.post('/notas/borrar/{notas_id}')
def borarNotas(notas_id: int):
    ver = FuncionesDB()
    ver.borrarRegistro("notas", notas_id)

    return {"message": "Registro borrado correctamente"}