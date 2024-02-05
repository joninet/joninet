from fastapi import APIRouter, HTTPException, Query, Path
from models.product import Product
from config import dbconn
from helpers.functions_db import printData, insertData
import random
from datetime import datetime

routerEntry = APIRouter()

@routerEntry.get('/entryproduct/{code}/{quantity}/{warehouse}/{supplier}/{invoice}')
async def entryProduct(
    code: int = Path(..., title="Código del producto", ge=0),
    quantity: float = Path(..., title="Cantidad del producto", ge=0),
    warehouse: str = Path(..., title="Almacén"),
    supplier: str = Path(..., title="Proveedor"),
    invoice: str = Path(..., title="Factura"),
):
    codeSearch=printData(dbconn, code, "code", "products", "code")

    if codeSearch is not None:
        d = datetime.now()
        dateEntry=d.strftime("%Y-%m-%d %H:%M:%S")
        name=printData(dbconn, code, "name", "products", "code")
        um=printData(dbconn, code, "um", "products", "code")
        column = ["date", "code", "name", "um", "quantity", "warehouse", "supplier", "invoice"]
        values = [dateEntry, code, name, um, quantity, warehouse, supplier, invoice]
        
        insertData(dbconn, "entryproducts", column, values)

        return {"message": "Entry successfully"}
    else:
        return {"message": "no existe el codigo"}
