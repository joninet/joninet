from fastapi import APIRouter, HTTPException, Query, Path
from models.product import Product
from config import dbconn
from helpers.functions_db import insertData, viewRow, editRow, printData, deleteRow, viewRowLimit
from helpers.functions_other import randomCode
import random

router = APIRouter()

@router.post('/products')
def createProduct(product: Product):
    column = ["name", "code", "stock", "typeProduct", "um"]
    if not product.code:
        product.code = randomCode()

    values = [product.name, product.code, product.stock, product.typeProduct, product.um]

    try:
        insertData(dbconn, "products", column, values)
        return {"message": "Product created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create product: {str(e)}")
    
@router.get('/products/{id}')
def getProduct(id: int = Path(gt=0)):
    return viewRow(dbconn, id, "products")

@router.get('/products')
def getProductsLimit():
    return viewRowLimit(dbconn, "products", 9000)

@router.put('/products/{id}')
def updateProduct(id: int, product: Product):
    code=printData(dbconn, id, "code","products","id")

    if product.code is None:
        column = ["name", "code", "stock", "typeProduct", "um"]
        values = [product.name, code, product.stock, product.typeProduct, product.um]

        editRow(dbconn, "products", column, values, f"id = ?", (id,))

        return {"message": "Product edit successfully"}
    else:
        return {"message": "Failed to create product: the code cannot be edited"}
    
@router.delete('/products/{id}')
def deleteProduct(id: int):
    return deleteRow(dbconn,"products",id)
