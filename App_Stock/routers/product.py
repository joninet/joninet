from fastapi import APIRouter, HTTPException, Query, Path
from models.product import Product
from config import dbconn
from helpers.functions_db import insertData, viewRow

router = APIRouter()

@router.post('/products')
def createProduct(product: Product):
    column = ["name", "code", "stock", "typeProduct", "um"]
    values = [product.name, product.code, product.stock, product.typeProduct, product.um]

    try:
        insertData(dbconn, "products", column, values)
        return {"message": "Product created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create product: {str(e)}")
    
@router.get('/products/{id}')
def getProduct(id: int = Path(gt=0)):
    return viewRow(dbconn, id, "products")



