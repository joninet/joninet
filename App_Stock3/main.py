from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from helpers.funciones_db import FuncionesDB
from routers.productos import router as productRouter
from routers.index import router as index
from routers.proveedores import router as proveedorRouter
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(productRouter)
app.include_router(index)
app.include_router(proveedorRouter)

app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")





