from fastapi import APIRouter, HTTPException, Query, Path
from typing import Optional
from models.product import Product
from config import dbconn
from helpers.functions_db import printData, insertData, deleteRow, viewRow
import random
from datetime import datetime

router = APIRouter()

@router.get('/entryproduct/{code}/{quantity}/{warehouse}/{supplier}/{invoice}/comment')
async def entryProduct(
    code: int = Path(..., title="Código del producto", ge=0, max_length=20),
    quantity: float = Path(..., title="Cantidad del producto", ge=0),
    warehouse: str = Path(..., title="Almacén"),
    supplier: str = Path(..., title="Proveedor"),
    invoice: str = Path(..., title="Factura"),
    comment: Optional[str] = None
):
    codeSearch=printData(dbconn, code, "code", "products", "code")

    if codeSearch is not None:
        d = datetime.now()
        dateEntry=d.strftime("%Y-%m-%d %H:%M:%S")
        name=printData(dbconn, code, "name", "products", "code")
        um=printData(dbconn, code, "um", "products", "code")
        if comment is not None:
            column = ["date", "code", "name", "um", "quantity", "warehouse", "supplier", "invoice","comment"]
            values = [dateEntry, code, name, um, quantity, warehouse, supplier, invoice, comment]
        else:
            column = ["date", "code", "name", "um", "quantity", "warehouse", "supplier", "invoice"]
            values = [dateEntry, code, name, um, quantity, warehouse, supplier, invoice]
        
        insertData(dbconn, "entryproducts", column, values)
        return {"message": "Entry successfully"}
    else:
        return {"message": "The code does not exist"}
    
@router.delete('/entryproduct/{id}')
def deleteEntryProduct(id: int):
    return deleteRow(dbconn, "entryproducts",id)

@router.get('/entryproduct/{id}')
def getEntryProduct(id: int = Path(gt=0)):
    return viewRow(dbconn, id, "entryproducts")



