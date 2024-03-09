from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette.responses import HTMLResponse
import sqlite3
from routers.eliminar import router as eliminar

app = FastAPI()
app.include_router(eliminar)

