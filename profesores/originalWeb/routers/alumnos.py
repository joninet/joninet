from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/alumnos/nuevo", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoProducto(req: Request):
  verDb = FuncionesDB()
  colegios = verDb.mostrarTabla("colegios")
  grados = verDb.mostrarTabla("grados")
  return template.TemplateResponse("alumnos_nuevo.html", {"request": req, "colegios": colegios, "grados": grados})

@router.post('/alumnos/crear')
async def crearAlumnos(
    req: Request,
    nombres: str = Form(None),
    apellidos: str = Form(None),
    email: str = Form(None),
    id_grados: int = Form(None),
    id_colegios: int = Form(None)):

    nombres = nombres.upper()
    apellidos = apellidos.upper()


    column = ["nombres", "apellidos", "email", "id_colegios", "id_grados"]
    values = [nombres, apellidos, email, id_colegios, id_grados]

    verDb = FuncionesDB()
    verDb.insertarDatos("alumnos", column, values)

    colegios = verDb.mostrarTabla("colegios")
    grados = verDb.mostrarTabla("grados")

    info_mensaje = "El Alumno fue creado exitosamente"
    return template.TemplateResponse("alumnos_nuevo.html", {"request": req, "info_mensaje": info_mensaje, "colegios": colegios, "grados": grados})

@router.get("/alumnos/ver")
def verAlumnos(req:Request, page: int = 1):
    verDb = FuncionesDB()
    colegios = verDb.mostrarTabla("colegios")
    grados = verDb.mostrarTabla("grados")
    alumnos = verDb.mostrarTablaPaginada("alumnos", page, 15)
    total_productos = verDb.contarFilas("alumnos")
    total_paginas = math.ceil(total_productos / 15)
    return template.TemplateResponse("alumnos_ver.html", { "request" : req, "colegios": colegios, "alumnos": alumnos, "grados": grados,"page": page, "total_paginas": total_paginas })

@router.get('/alumnos/borrar/{alumnos_id}')
def borarAlumno(req: Request, alumnos_id: int, page: int = 1):
    verDb = FuncionesDB()
    verDb.borrarRegistro("alumnos", alumnos_id)
    return RedirectResponse(url="/alumnos/ver")