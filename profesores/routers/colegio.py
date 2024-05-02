from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse
from helpers.funciones_db import FuncionesDB
import sqlite3

router = APIRouter()

@router.post('/colegio/crear')
async def crearIngreso(
    req: Request,
    nombre: str = Form(None)):

    column = ["nombre"]
    values = [nombre]

    insertar = FuncionesDB()
    insertar.insertarDatos("colegios", column, values)

    return {"message": "creado"}