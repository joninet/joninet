from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from helpers.funciones_db import FuncionesDB
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/productos/nuevo", response_class=HTMLResponse)
def nuevoProducto(req: Request):
  verDB = FuncionesDB()
  categorias= verDB.mostrarTabla("Categoria")
  #print(categorias)
  return template.TemplateResponse("nuevo_producto.html", {"request": req, "categorias": categorias})

@router.delete("/productos/borrar/{producto_id}")
def borrarProducto(producto_id: int, req: Request):
    verDB = FuncionesDB()
    borrar = verDB.borrarDatos("Producto", producto_id)
    return template.TemplateResponse("datosActualizados.html", {"request": req})


@router.post('/productos/crear')
async def crearProducto(
    req: Request,
    nombre: str = Form(None),
    um: str = Form(None),
    descripcion: str = Form(None),
    categoria_id: int = Form(None)):

    if not (nombre and um and descripcion and categoria_id):
        error_msg = "Por favor, complete todos los campos."
        verDB = FuncionesDB()
        categorias= verDB.mostrarTabla("Categoria")
        return template.TemplateResponse(
            "nuevo_producto.html", 
            {"request": req, "errorIngresoInsumo": error_msg, "nombre": nombre, "um": um, "descripcion": descripcion, "categoria_id": categoria_id, "categorias": categorias}
        )

    column = ["nombre", "um", "descripcion", "categoria_id"]
    values = [nombre, um, descripcion, categoria_id]

    insertar = FuncionesDB()
    insertar.insertarDatos("Producto", column, values)
    return template.TemplateResponse("datosActualizados.html", {"request": req})

@router.get("/productos/ver_todos")
def verProductos(req:Request, page: int = 1):
    verDb = FuncionesDB()
    productos = verDb.mostrarTablaPaginada("Producto", page, 15)
    total_productos = verDb.contarFilas("Producto")
    total_paginas = math.ceil(total_productos / 15)
    categorias = verDb.mostrarTabla("Categoria")
    return template.TemplateResponse("productos.html", { "request" : req, "productos": productos, "categorias": categorias, "page": page, "total_paginas": total_paginas })
