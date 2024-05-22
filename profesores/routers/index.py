from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
import math
import sqlite3

router = APIRouter()

template = Jinja2Templates(directory="./templates")

@router.get("/", response_class=HTMLResponse)#indica que la ruta va a responder con contenido html
def nuevoProducto(req: Request):
  
  return template.TemplateResponse("index.html", {"request": req})
