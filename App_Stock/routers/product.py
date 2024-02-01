from fastapi import APIRouter, HTTPException
from models.product import Product
from config import dbconn
from helpers.functions_db import insertData

router = APIRouter()

@router.post('/products')
def createProduct(product: Product):
    columnas = ["name", "code", "stock", "typeProduct", "um"]
    valores = [product.name, product.code, product.stock, product.typeProduct, product.um]

    try:
        insertData(dbconn, "products", columnas, valores)
        return {"message": "Product created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create product: {str(e)}")



