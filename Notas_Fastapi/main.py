from fastapi import FastAPI, Form, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from starlette.middleware.sessions import SessionMiddleware
import bcrypt

# Inicializar la aplicación FastAPI
app = FastAPI()

# Añade una clave secreta para firmar las cookies de sesión
app.add_middleware(SessionMiddleware, secret_key="tu_secreto_aqui")

# Configurar las plantillas
templates = Jinja2Templates(directory="templates")

# Configurar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar la base de datos usando SQLAlchemy con SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./notas.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definir modelos de SQLAlchemy
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String, unique=True, index=True)
    contrasena = Column(String)

class Nota(Base):
    __tablename__ = "notas"
    id = Column(Integer, primary_key=True, index=True)
    contenido = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="notas")

Usuario.notas = relationship("Nota", back_populates="usuario")

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Función para obtener la sesión de base de datos
def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Páginas y endpoints
@app.get("/", response_class=HTMLResponse)
async def leer_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/registro", response_class=HTMLResponse)
async def form_registro(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/registro")
async def registro(nombre_usuario: str = Form(...), contrasena: str = Form(...), db: Session = Depends(obtener_db)):
    # Hashear la contraseña
    hashed_contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

    # Crear usuario en la base de datos
    db_usuario = Usuario(nombre_usuario=nombre_usuario, contrasena=hashed_contrasena.decode('utf-8'))
    db.add(db_usuario)
    try:
        db.commit()
    except:
        db.rollback()
        raise HTTPException(status_code=400, detail="Nombre de usuario ya registrado")

    return RedirectResponse(url="/login", status_code=303)

@app.get("/login", response_class=HTMLResponse)
async def form_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, nombre_usuario: str = Form(...), contrasena: str = Form(...), db: Session = Depends(obtener_db)):
    # Buscar usuario en la base de datos
    usuario = db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first()

    # Verificar contraseña
    if usuario and bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8')):
        request.session['usuario_id'] = usuario.id
        return RedirectResponse(url="/notas", status_code=303)
    else:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

@app.get("/notas", response_class=HTMLResponse)
async def leer_notas(request: Request, db: Session = Depends(obtener_db)):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return RedirectResponse(url="/login", status_code=303)

    # Obtener notas del usuario actual
    notas = db.query(Nota).filter(Nota.usuario_id == usuario_id).all()

    return templates.TemplateResponse("notas.html", {"request": request, "notas": notas})

@app.post("/notas")
async def agregar_nota(request: Request, contenido: str = Form(...), db: Session = Depends(obtener_db)):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return RedirectResponse(url="/login", status_code=303)

    # Crear nueva nota
    nueva_nota = Nota(usuario_id=usuario_id, contenido=contenido)
    db.add(nueva_nota)
    db.commit()

    return RedirectResponse(url="/notas", status_code=303)
