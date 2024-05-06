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
  parciales = verDb.mostrarTabla("parciales")
  colegios = verDb.mostrarTabla("colegios")
  grados = verDb.mostrarTabla("grados")

  return template.TemplateResponse("condiciones_nuevo.html", {"request": req, "parciales": parciales, "colegios": colegios, "grados": grados})

@router.post("/condiciones/consultar")
async def condicionesConsultar(
  req: Request,
  id_parcial: int = Form(None),
  estado: str = Form(None)):
  resultados = []
  verDb = FuncionesDB()
  parciales = verDb.mostrarTabla("parciales")
  colegios = verDb.mostrarTabla("colegios")
  grados = verDb.mostrarTabla("grados")
  notas = verDb.mostrarTabla("notas")

  if estado == "aprobado":
      for x in notas:
          if x[2] >= 5 and x[7] == id_parcial:
              resultados.append({"nota": x[2]})
  else:
      for x in notas:
          if x[2] <= 5 and x[7] == id_parcial:
              resultados.append({"nota": x[2]})

  print(resultados)
    
  return template.TemplateResponse("condiciones_mostrar.html", {"request": req, "resultados": resultados})


  




  