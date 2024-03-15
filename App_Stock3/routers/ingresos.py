from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
from datetime import datetime
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/ingresos/nuevo", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoProducto(req: Request):
  verDB = FuncionesDB()
  categorias= verDB.mostrarTabla("Categoria")
  producto= verDB.mostrarTabla("Producto")
  proveedor= verDB.mostrarTabla("Proveedor")
  estado= verDB.mostrarTabla("Estado")
  almacen= verDB.mostrarTabla("Almacen")
  usuario= verDB.mostrarTabla("Usuario")
  #print(categorias)
  return template.TemplateResponse("ingresos_nuevo.html", {"request": req, "categorias": categorias, "producto": producto, "proveedor": proveedor, "estado": estado, "almacen": almacen, "usuario": usuario})

@router.post('/ingresos/crear')
async def crearIngreso(
    req: Request,
    producto_id: int = Form(None),
    cantidad: float = Form(None),
    proveedor_id: int = Form(None),
    oc: str = Form(None),
    lote: str = Form(None),
    vto: str = Form(None),
    estado_id: int = Form(None),
    remito: str = Form(None),
    usuario_id: int = Form(None),
    almacen_id: int = Form(None)):

    verDB = FuncionesDB()
    producto=verDB.seleccionarDatos("Producto",producto_id)
    proveedor=verDB.seleccionarDatos("Proveedor",proveedor_id)
    estado=verDB.seleccionarDatos("Estado", estado_id)
    usuario=verDB.seleccionarDatos("Usuario", usuario_id)
    almacen=verDB.seleccionarDatos("Almacen", almacen_id)

    if producto == None and  proveedor==None and  estado==None and usuario==None and almacen==None:
      error_msg = "id Inexistente"
      return template.TemplateResponse(
            "ingresos_nuevo.html", 
            {"request": req, "errorIngresoInsumo": error_msg, "producto_id": producto_id, "cantidad": cantidad, "proveedor_id": proveedor_id, "oc": oc, "lote": lote, "vto": vto, 
             "estado_id": estado_id, "remito": remito, "usuario_id": usuario_id, "almacen_id": almacen_id}
        )

    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    column = ["producto_id", "cantidad", "proveedor_id", "oc", "lote", "vto", "estado_id", "remito", "usuario_id", "almacen_id", "fecha"]
    values = [producto_id, cantidad, proveedor_id, oc, lote, vto, estado_id, remito, usuario_id, almacen_id, fecha_actual]

    insertar = FuncionesDB()
    insertar.insertarDatos("Ingresos", column, values)
    return template.TemplateResponse("datosActualizados.html", {"request": req})