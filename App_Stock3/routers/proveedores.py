from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
import datetime
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/proveedores/nuevo", response_class=HTMLResponse)
def proveedoresNuevo(req:Request):
    return template.TemplateResponse("proveedores_nuevo.html", {"request": req})

@router.post("/proveedores/crear")
async def proveedoresCrear(req: Request, 
                           nombre: str = Form(None),
                           direccion: str = Form(None),
                           localidad: str = Form(None),
                           telefono: str = Form(None),
                           email: str = Form(None),
                           moneda: str = Form(None)
                           ):
    if not (nombre and direccion and localidad and telefono and email and moneda):
        error_msg = "Por favor, complete todos los campos."
        return template.TemplateResponse(
            "proveedores_nuevo.html", 
            {"request": req, "errorIngresoInsumo": error_msg, "nombre": nombre, "direccion": direccion, "localidad": localidad, "telefono": telefono, "email": email, "moneda": moneda}
        )
    fechaActual =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    column = ["nombre", "direccion", "localidad", "telefono", "email", "moneda", "fecha"]
    values = [nombre, direccion, localidad, telefono, email, moneda, fechaActual]

    insertar = FuncionesDB()
    insertar.insertarDatos("Proveedor", column, values)
    return template.TemplateResponse("datosActualizados.html", {"request": req})