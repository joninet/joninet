from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.session import SessionMiddleware
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="secret_key")

templates = Jinja2Templates(directory="templates")

# Diccionario en memoria simulando una base de datos
usuarios = {"usuario1": "contraseña1", "usuario2": "contraseña2"}

def verificar_sesion(request: Request):
    if "usuario" not in request.session:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="No estás logueado")

@app.get("/", response_class=HTMLResponse)
@app.post("/", response_class=HTMLResponse)
async def login(request: Request, usuario: str = Form(None), contraseña: str = Form(None)):
    if request.method == "POST":
        if usuario in usuarios and usuarios[usuario] == contraseña:
            # Autenticación exitosa, establecer variable de sesión
            request.session["usuario"] = usuario
            return RedirectResponse("/stock")
        else:
            # Credenciales incorrectas, mostrar mensaje de error en index.html
            return templates.TemplateResponse("index.html", {"request": request, "error": "Credenciales incorrectas"})
    # Si la solicitud es GET, mostrar la página de inicio
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/stock", response_class=HTMLResponse, dependencies=[Depends(verificar_sesion)])
async def stock(request: Request):
    return templates.TemplateResponse("stock.html", {"request": request})

@app.get("/producto", response_class=HTMLResponse, dependencies=[Depends(verificar_sesion)])
async def producto(request: Request):
    return templates.TemplateResponse("producto.html", {"request": request})
