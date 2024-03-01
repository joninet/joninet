from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from helpers.funciones_db import FuncionesDB
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/productos/nuevo", response_class=HTMLResponse)
def nuevoProducto(req: Request):
  verDB = FuncionesDB()
  categorias= verDB.mostrarTabla("Categoria")
  #print(categorias)
  return template.TemplateResponse("nuevo_producto.html", {"request": req, "categorias": categorias})

@router.post('/productos/crear')
async def crear_producto(
    req: Request,
    nombre: str = Form(...),
    um: str = Form(...),
    descripcion: str = Form(...),
    categoria_id: int = Form(...)):

    if nombre and um and descripcion and categoria_id:

      column = ["nombre", "um", "descripcion", "categoria_id"]
      values = [nombre, um, descripcion, categoria_id]

      insertar = FuncionesDB()
      insertar.insertarDatos("Producto", column, values)
      return template.TemplateResponse("datosActualizados.html", {"request": req})
    else:
      return template.TemplateResponse("/productos/crear", {"errorIngresoInsumo": "Las credenciales no son correctas o existen campos vacios"})