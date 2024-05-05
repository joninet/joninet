from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
from datetime import datetime
import json
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/notas/nuevo", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoNotas(req: Request):
  verDb = FuncionesDB()
  alumnos = verDb.mostrarTabla("alumnos")
  parciales = verDb.mostrarTabla("parciales")
  return template.TemplateResponse("notas_nuevo.html", {"request": req, "alumnos": alumnos, "parciales": parciales})

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

    verDb = FuncionesDB()
    verDb.insertarDatos("notas", column, values)
    alumnos = verDb.mostrarTabla("alumnos")
    parciales = verDb.mostrarTabla("parciales")

    info_mensaje = "La nota fue creada exitosamente"
    return template.TemplateResponse("notas_nuevo.html", {"request": req, "info_mensaje": info_mensaje, "alumnos": alumnos, "parciales": parciales})

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

@router.get("/notas/ver")
def verNotas(req:Request, page: int = 1):
    verDb = FuncionesDB()

    alumnos = verDb.mostrarTabla("alumnos")
    parciales = verDb.mostrarTabla("parciales")
    colegios = verDb.mostrarTabla("colegios")
    materias = verDb.mostrarTabla("materias")
    grados = verDb.mostrarTabla("grados")
    notas2 = verDb.mostrarTabla("notas")

    resultados=[]

    for x in notas2:
        codigo = x[0]
        fecha = x[1]
        nota = x[2]
        rec1 = x[3]
        rec2 = x[4]
        rec3 = x[5]
        for alumno in alumnos:
            if alumno[0] == x[6]:
                alumno_nombre = alumno[2]
        for parcial in parciales:
            if parcial[0] == x[7]:
                parcial_nombre = parcial[1]
                for materia in materias:
                    if materia[0] == parcial[2]:
                        materia_nombre=materia[1]
                        for colegio in colegios:
                            if colegio[0] == materia[2]:
                                colegio_nombre = colegio[1]
                        for grado in grados:
                            if grado[0] == materia[3]:
                                grado_nombre = grado[1] + grado[2]

        resultados.append({
        "codigo": codigo,
        "fecha": fecha,
        "nota": nota,
        "rec1": rec1,
        "rec2": rec2,
        "rec3": rec3,
        "alumnoNombre": alumno_nombre,
        "parcialNombre": parcial_nombre,
        "materiaNombre": materia_nombre,
        "colegioNombre": colegio_nombre,
        "gradoNombre": grado_nombre})
        
    notas = verDb.mostrarTablaPaginada("notas", page, 15)
    total_notas = verDb.contarFilas("notas")
    total_paginas = math.ceil(total_notas / 15)
    return template.TemplateResponse("notas_ver.html", { "request" : req, "resultados": resultados, "notas": notas, "page": page, "total_paginas": total_paginas })


@router.get('/notas/borrar/{notas_id}')
def borarParciales(req: Request, notas_id: int, page: int = 1):
    verDb = FuncionesDB()
    alumnos = verDb.mostrarTabla("alumnos")
    parciales = verDb.mostrarTabla("parciales")
    verDb.borrarRegistro("notas", notas_id)
    notas = verDb.mostrarTablaPaginada("notas", page, 15)
    total_notas = verDb.contarFilas("notas")
    total_paginas = math.ceil(total_notas / 15)

    info_mensaje = "La nota fue borrada exitosamente"
    return template.TemplateResponse("notas_ver.html", { "request" : req, "info_mensaje": info_mensaje, "alumnos": alumnos, "parciales": parciales, "notas": notas, "page": page, "total_paginas": total_paginas })
