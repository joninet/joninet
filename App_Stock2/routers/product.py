from fastapi import APIRouter, HTTPException, Query, Path
from models.product import Product
from helpers.functions_other import randomCode
from helpers.handle_db import HandleDB

router = APIRouter()

@router.post('/products')
def createProduct(product: Product):
    column = ["name", "code", "stock", "typeProduct", "um"]
    if not product.code:
        product.code = randomCode()

    values = [product.name, product.code, product.stock, product.typeProduct, product.um]

    try:
        db = HandleDB()
        db.insertData("products", column, values)
        return {"message": "Product created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create product: {str(e)}")

#funcion para mostrar un registro segun su id
@router.get('/products/{id}')
def getProduct(id: int = Path(gt=0)):
    db = HandleDB()
    return db.viewRow(id, "products")

#funcion para mostrar varios registros segun limite
@router.get('/products')
def getProductsLimit():
    db = HandleDB()
    return db.viewRowLimit("products", 9000)

#funcion para editar un producto
@router.put('/products/{id}')
def updateProduct(id: int, product: Product):
    db = HandleDB()
    code=db.printData(id, "code","products","id")

    if product.code is None:
        column = ["name", "code", "stock", "typeProduct", "um"]
        values = [product.name, code, product.stock, product.typeProduct, product.um]

        db.editRow("products", column, values, f"id = ?", (id,))

        return {"message": "Product edit successfully"}
    else:
        return {"message": "Failed to create product: the code cannot be edited"}
    
@router.delete('/products/{id}')
def deleteProduct(id: int):
    db = HandleDB()
    return db.deleteRow("products",id)

