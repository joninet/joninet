from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/condiciones/nuevo", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoCondiciones(req: Request):
  verDb = FuncionesDB()
  materias = verDb.mostrarTabla("materias")
  colegios = verDb.mostrarTabla("colegios")
  grados = verDb.mostrarTabla("grados")

  return template.TemplateResponse("condiciones_nuevo.html", {"request": req, "materias": materias, "colegios": colegios, "grados": grados})

@router.post("/condiciones/consultar")
async def condicionesConsultar(
  req: Request,
  id_materias: int = Form(None),
  id_colegios: str = Form(None),
  id_grados: float = Form(None),
  estado: str = Form(None)):
  resultados = []
  verDb = FuncionesDB()
  materias = verDb.mostrarTabla("materias")
  colegios = verDb.mostrarTabla("colegios")
  grados = verDb.mostrarTabla("grados")
  notas = verDb.mostrarTabla("notas")

  if estado == "aprobados":
    for x in notas:
      if x[2] >= 5:
        notass = x[2]
        resultado.append({"nota": notass})
    
  return template.TemplateResponse("condiciones_mostrar.html", {"request": req, "resultados": resultados})


  




  