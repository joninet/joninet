from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
import math
from datetime import datetime
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/parciales/nuevo", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoParciales(req: Request):
  verDb = FuncionesDB()
  colegios = verDb.mostrarTabla("colegios")
  materias = verDb.mostrarTabla("materias")
  grados = verDb.mostrarTabla("grados")
  return template.TemplateResponse("parciales_nuevo.html", {"request": req, "colegios": colegios, "materias": materias, "grados": grados})

@router.post('/parciales/crear')
async def crearParciales(
    req: Request,
    tema: str = Form(None),
    fecha: str = Form(None),
    id_materia: int = Form(None)):

    tema = tema.upper()
    fecha_datetime = datetime.strptime(fecha, "%d-%m-%Y")

    column = ["tema", "id_materias", "fecha"]
    values = [tema, id_materia, fecha_datetime]

    verDb = FuncionesDB()
    verDb.insertarDatos("parciales", column, values)

    colegios = verDb.mostrarTabla("colegios")
    materias = verDb.mostrarTabla("materias")
    grados = verDb.mostrarTabla("grados")

    info_mensaje = "El parcial fue creada exitosamente"

    return template.TemplateResponse("parciales_nuevo.html", {"request": req, "info_mensaje": info_mensaje, "colegios": colegios, "materias": materias, "grados": grados})

@router.get("/parciales/ver")
def verparciales(req: Request, page: int = 1):
    verDb = FuncionesDB()

    colegios = verDb.mostrarTabla("colegios")
    materias = verDb.mostrarTabla("materias")
    grados = verDb.mostrarTabla("grados")
    parciales2 = verDb.mostrarTabla("parciales")
    resultados = []

    for x in parciales2:
        codigo = x[0]
        tema = x[1]
        fecha = str(x[3])
        fechaSinHora = fecha.split(" ")[0]
        
        materiaNombre = None
        colegioNombre = None
        gradoNombre = None

        for materia in materias:
            if materia[0] == x[2]:
                materiaNombre = materia[1]
                for colegio in colegios:
                    if colegio[0] == materia[2]:
                        colegioNombre = colegio[1]
                for grado in grados:
                    if grado[0] == materia[3]:
                        gradoNombre = grado[1] + grado[2]
        
        if materiaNombre and colegioNombre and gradoNombre:
            resultados.append({
                "codigo": codigo,
                "tema": tema,
                "materia": materiaNombre,
                "colegio": colegioNombre,
                "fecha": fechaSinHora,
                "grado": gradoNombre
            })

    parciales = verDb.mostrarTablaPaginada("parciales", page, 15)
    total_parciales = verDb.contarFilas("parciales")
    total_paginas = math.ceil(total_parciales / 15)

    return template.TemplateResponse("parciales_ver.html", {
        "request": req,
        "resultados": resultados,
        "parciales": parciales,
        "page": page,
        "total_paginas": total_paginas
    })

@router.get('/parciales/borrar/{parciales_id}')
def borarParciales(req: Request, parciales_id: int, page: int = 1):
    verDb = FuncionesDB()
    verDb.borrarRegistro("parciales", parciales_id)
    return RedirectResponse(url="/parciales/ver")