from fastapi import APIRouter, FastAPI, Request, Response, Form, Query, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from helpers.funciones_db import FuncionesDB
from fastapi.responses import FileResponse
import math
import sqlite3

router = APIRouter()

@router.get("/bajardb")
async def download_db():
    file_path = "profesordb.db"
    return FileResponse(file_path, filename="profesordb.db")