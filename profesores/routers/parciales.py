from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/parciales/nuevo", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoParciales(req: Request):
  verDb = FuncionesDB()
  colegios = verDb.mostrarTabla("colegios")
  materias = verDb.mostrarTabla("materias")
  return template.TemplateResponse("parciales_nuevo.html", {"request": req, "colegios": colegios, "materias": materias})

@router.post('/parciales/crear')
async def crearParciales(
    req: Request,
    tema: str = Form(None),
    id_materia: int = Form(None),
    id_colegio: int = Form(None)):

    tema = tema.upper()

    column = ["tema", "id_materia", "id_colegio"]
    values = [tema, id_materia, id_colegio]

    verDb = FuncionesDB()
    verDb.insertarDatos("parciales", column, values)

    colegios = verDb.mostrarTabla("colegios")
    materias = verDb.mostrarTabla("materias")

    info_mensaje = "El parcial fue creada exitosamente"
    return template.TemplateResponse("parciales_nuevo.html", {"request": req, "info_mensaje": info_mensaje,"colegios": colegios, "materias": materias})

@router.get("/parciales/ver")
def verMaterias(req:Request, page: int = 1):
    verDb = FuncionesDB()
    materias = verDb.mostrarTabla("materias")
    colegios = verDb.mostrarTabla("colegios")
    parciales = verDb.mostrarTablaPaginada("parciales", page, 15)
    total_parciales = verDb.contarFilas("parciales")
    total_paginas = math.ceil(total_parciales / 15)
    return template.TemplateResponse("parciales_ver.html", { "request" : req, "colegios": colegios, "parciales": parciales, "materias": materias, "page": page, "total_paginas": total_paginas })


@router.get('/parciales/borrar/{parciales_id}')
def borarParciales(req: Request, parciales_id: int, page: int = 1):
    verDb = FuncionesDB()
    materias = verDb.mostrarTabla("materias")
    colegios = verDb.mostrarTabla("colegios")
    verDb.borrarRegistro("parciales", parciales_id)
    parciales = verDb.mostrarTablaPaginada("parciales", page, 15)
    total_parciales = verDb.contarFilas("parciales")
    total_paginas = math.ceil(total_parciales / 15)

    info_mensaje = "El parcial fue borrada exitosamente"
    return template.TemplateResponse("materias_ver.html", { "request" : req, "info_mensaje": info_mensaje, "colegios": colegios, "parciales": parciales, "materias": materias, "page": page, "total_paginas": total_paginas })
