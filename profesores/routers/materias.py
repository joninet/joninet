from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/materias/nuevo", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoMaterias(req: Request):
  verDb = FuncionesDB()
  colegios = verDb.mostrarTabla("colegios")
  grados = verDb.mostrarTabla("grados")
  return template.TemplateResponse("materias_nuevo.html", {"request": req, "colegios": colegios, "grados": grados})

@router.post('/materias/crear')
async def crearMaterias(
    req: Request,
    nombre: str = Form(None),
    id_colegio: int = Form(None),
    id_grado: int = Form(None)):

    nombre = nombre.upper()

    column = ["nombre", "id_colegio", "id_grado"]
    values = [nombre, id_colegio, id_grado]

    verDb = FuncionesDB()
    verDb.insertarDatos("materias", column, values)
    colegios = verDb.mostrarTabla("colegios")
    grados = verDb.mostrarTabla("grados")

    info_mensaje = "La materia fue creada exitosamente"

    return template.TemplateResponse("materias_nuevo.html", {"request": req, "info_mensaje": info_mensaje,"colegios": colegios, "grados": grados})

@router.get("/materias/ver")
def verMaterias(req:Request, page: int = 1):
    verDb = FuncionesDB()
    materias = verDb.mostrarTabla("materias")
    colegios = verDb.mostrarTabla("colegios")
    grados = verDb.mostrarTabla("grados")
    materias = verDb.mostrarTablaPaginada("materias", page, 15)
    total_materias = verDb.contarFilas("materias")
    total_paginas = math.ceil(total_materias / 15)
    return template.TemplateResponse("materias_ver.html", { "request" : req, "colegios": colegios, "grados": grados, "materias": materias, "page": page, "total_paginas": total_paginas })

@router.get('/materias/borrar/{materias_id}')
def borarMaterias(req: Request, materias_id: int, page: int = 1):
    verDb = FuncionesDB()
    verDb.borrarRegistro("materias", materias_id)
    return RedirectResponse(url="/materias/ver")