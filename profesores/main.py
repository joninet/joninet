from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from helpers.funciones_db import FuncionesDB
from routers.colegio import router as colegioRouter
from routers.grados import router as gradosRouter
from routers.materias import router as materiasRouter
from routers.alumnos import router as alumnosRouter
from routers.parciales import router as parcialesRouter
from routers.notas import router as notasRouter



from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(colegioRouter)
app.include_router(gradosRouter)
app.include_router(materiasRouter)
app.include_router(alumnosRouter)
app.include_router(parcialesRouter)
app.include_router(notasRouter)



