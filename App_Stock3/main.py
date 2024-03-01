from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from helpers.funciones_db import FuncionesDB
from routers.productos import router as productRouter
from routers.index import router as index

app=FastAPI()
app.include_router(productRouter)
app.include_router(index)



