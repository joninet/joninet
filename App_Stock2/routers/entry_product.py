from fastapi import APIRouter, HTTPException, Query, Path
from typing import Optional
from models.product import Product
from config import dbconn
from helpers.handle_db import HandleDB
import random
from datetime import datetime

router = APIRouter()

# Función para registrar la entrada de un producto
@router.get('/entryproduct/{code}/{quantity}/{warehouse}/{supplier}/{invoice}/comment')
async def entryProduct(
    code: int = Path(..., title="Código del producto", ge=0),
    quantity: float = Path(..., title="Cantidad del producto", ge=0),
    warehouse: str = Path(..., title="Almacén"),
    supplier: str = Path(..., title="Proveedor"),
    invoice: str = Path(..., title="Factura"),
    comment: Optional[str] = None
):
    
    # Verificamos si el codigo que se envio existe 
    db = HandleDB()
    codeSearch = db.printData(code, "code", "products", "code")

    if codeSearch is not None:
        d = datetime.now()
        dateEntry=d.strftime("%Y-%m-%d %H:%M:%S")

        # Obtenemos el nombre y la unidad de medida del producto segun el codigo
        name = db.printData(code, "name", "products", "code")
        um = db.printData(code, "um", "products", "code")

        #verificamos si el registro tiene comentarios
        if comment is not None:
            column = ["date", "code", "name", "um", "quantity", "warehouse", "supplier", "invoice","comment"]
            values = [dateEntry, code, name, um, quantity, warehouse, supplier, invoice, comment]
        else:
            column = ["date", "code", "name", "um", "quantity", "warehouse", "supplier", "invoice"]
            values = [dateEntry, code, name, um, quantity, warehouse, supplier, invoice]
        
        #insertamos el registro en la db
        db.insertData("entryproducts", column, values)
        return {"message": "Entry successfully"}
    else:
        return {"message": "The code does not exist"}
    
#Funcion para borrar un registro en la db segun su id
@router.delete('/entryproduct/{id}')
def deleteEntryProduct(id: int):
    db = HandleDB()
    return db.deleteRow(dbconn, "entryproducts",id)

#Funcion para imprimir datos de un registro de la db segun su id
@router.get('/entryproduct/{id}')
def getEntryProduct(id: int = Path(gt=0)):
    db = HandleDB()
    return db.viewRow(dbconn, id, "entryproducts")

#Funcion para imprimir datos de una tabla
@router.get('/entryproduct')
def getAllEntryProduct():
    db = HandleDB()
    return db.viewRowLimit(dbconn, "entryproducts", 9000)