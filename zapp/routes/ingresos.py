from fastapi import APIRouter, Depends
from db.ingresos import conectar_base_datos, insertar_ingreso, obtener_ingresos
from models.ingreso import Ingreso

router = APIRouter()

@router.post("/ingresar")
async def ingresar(ingreso: Ingreso):
    with conectar_base_datos() as connection:
        insertar_ingreso(connection, ingreso)
    return {"message": "Ingreso registrado correctamente."}

@router.get("/ingresos")
def obtener_ingresos():
    with conectar_base_datos() as connection:
        ingresos = obtener_ingresos(connection)
    return ingresos