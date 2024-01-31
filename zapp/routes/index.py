from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def index():
    return {"message": "Bienvenido al sistema de registro de ingresos."}