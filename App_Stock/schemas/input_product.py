from schemas.product import Product
from datetime import datetime

class InputProduct(Product, only=["code", "name","productType","um"]):
    quantity: float
    provider: str
    oc: str
    batch: str
    expirationDate: str
    user: str
    date: str
    invoice: str