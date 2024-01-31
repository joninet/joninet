from fastapi import APIRouter, Query, Path
from models.product import Product
from config import dbconn
from helpers.functions_db import insertData
router = APIRouter()

@router.post('/products')
def createProduct(product: Product):
    columnas = ["name", "code", "stock", "typeProduct", "um"]
    valores = [product.name, product.code, product.stock, product.typeProduct, product.um]
    insertData(dbconn, "products", columnas, valores)


