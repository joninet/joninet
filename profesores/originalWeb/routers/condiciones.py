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
   desde: float = Form(None),
   hasta: float = Form(None)):
   resultados = []
   verDb = FuncionesDB()
   parciales = verDb.mostrarTabla("parciales")
   colegios = verDb.mostrarTabla("colegios")
   grados = verDb.mostrarTabla("grados")
   notas = verDb.mostrarTabla("notas")
   alumnos = verDb.mostrarTabla("alumnos")

   for x in notas:
      if x[2] >= desde and x[2] <= hasta and x[7] == id_parcial:
         for i in alumnos:
            if x[6] == i[0]:
               for p in parciales:
                  if x[7] == p[0]:
                     resultados.append({"nota": x[2], "nombre": f"{i[2]}, {i[1]}", "parcial": p[1]})
    
   return template.TemplateResponse("condiciones_mostrar.html", {"request": req, "resultados": resultados})
  




  