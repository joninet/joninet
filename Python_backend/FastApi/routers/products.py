from fastapi import APIRouter

router=APIRouter(prefix="/products")

productsList=["Producto1","Producto2","Producto3","Producto4","Producto5"]

@router.get("/")
async def products():
    return productsList

@router.get("/{id}")
async def products(id: int):
    return productsList[id]
