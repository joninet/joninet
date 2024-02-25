# en producto.py dentro de la carpeta schemas o models
from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    um: str
    descripcion: str
    categoria_id: int
