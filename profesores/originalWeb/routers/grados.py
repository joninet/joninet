from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/grados/nuevo", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoProducto(req: Request):
  
  return template.TemplateResponse("grados_nuevo.html", {"request": req})

@router.post('/grados/crear')
async def crearGrados(
    req: Request,
    nombre: str = Form(None),
    division: str = Form(None)):

    division = division.upper()

    column = ["nombre", "division"]
    values = [nombre, division]

    insertar = FuncionesDB()
    insertar.insertarDatos("grados", column, values)

    info_mensaje = "El Grado fue creado exitosamente"
    return template.TemplateResponse("grados_nuevo.html", {"request": req, "info_mensaje": info_mensaje})


@router.get('/grados/borrar/{grados_id}')
def borarGrados(req: Request, grados_id: int, page: int = 1):
    verDb = FuncionesDB()
    verDb.borrarRegistro("grados", grados_id)
    return RedirectResponse(url="/grados/ver")

@router.get("/grados/ver")
def verGrados(req:Request, page: int = 1):
    verDb = FuncionesDB()
    grados = verDb.mostrarTablaPaginada("grados", page, 15)
    total_grados = verDb.contarFilas("grados")
    total_paginas = math.ceil(total_grados / 15)
    return template.TemplateResponse("grados_ver.html", { "request" : req, "grados": grados, "page": page, "total_paginas": total_paginas })
