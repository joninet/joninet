from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from helpers.funciones_db import FuncionesDB
from routers.colegio import router as colegioRouter

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(colegioRouter)