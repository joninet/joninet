from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/colegio/nuevo", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoProducto(req: Request):
  
  return template.TemplateResponse("colegio_nuevo.html", {"request": req})

@router.post('/colegio/crear')
async def crearColegio(
    req: Request,
    nombre: str = Form(None)):

    column = ["nombre"]
    values = [nombre]

    insertar = FuncionesDB()
    insertar.insertarDatos("colegios", column, values)

    info_mensaje = "El colegio fue creado exitosamente"
    return template.TemplateResponse("colegio_nuevo.html", {"request": req, "info_mensaje": info_mensaje})

@router.get('/colegio/borrar/{colegio_id}')
def borarColegio(req: Request, colegio_id: int, page: int = 1):
    verDb = FuncionesDB()
    verDb.borrarRegistro("colegios", colegio_id)
    colegios = verDb.mostrarTablaPaginada("colegios", page, 15)
    total_productos = verDb.contarFilas("colegios")
    total_paginas = math.ceil(total_productos / 15)

    info_mensaje = "El colegio fue borrado exitosamente"
    return template.TemplateResponse("colegio_ver.html", {"request": req, "info_mensaje": info_mensaje, "colegios": colegios, "page": page, "total_paginas": total_paginas})

@router.get("/colegio/ver")
def verColegios(req:Request, page: int = 1):
    verDb = FuncionesDB()
    colegios = verDb.mostrarTablaPaginada("colegios", page, 15)
    total_productos = verDb.contarFilas("colegios")
    total_paginas = math.ceil(total_productos / 15)
    return template.TemplateResponse("colegio_ver.html", { "request" : req, "colegios": colegios, "page": page, "total_paginas": total_paginas })
