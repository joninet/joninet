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

    column = ["fecha", "nota", "rec1", "rec2", "rec3", "id_alumno", "id_parcial"]
    values = [fecha, nota, rec1, rec2, rec3, id_alumno, id_parcial]

    insertar = FuncionesDB()
    insertar.insertarDatos("notas", column, values)

    return {"message": "creado"}