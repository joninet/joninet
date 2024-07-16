from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Base, Usuario, Nota
from routes import router
from database import crear_base_de_datos, obtener_conexion, cerrar_conexion

app = FastAPI(
    title="Aplicación de Notas",
    description="Aplicación para gestionar notas personales",
    version="1.0.0",
)

origins = ["*"]  # Ajustar para producción

app.add_middleware(
    CORSMiddleware(
        allow_origins=origins,
        allow_credentials=True,
        allow_headers=["*"],
        allow_methods=["*"],
    )
)

@app.on_event("startup")
def startup_event():
    crear_base_de_datos()

@app.on_event("shutdown")
def shutdown_event():
    conexion = obtener_conexion()
    cerrar_conexion(conexion)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
