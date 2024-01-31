from pydantic import BaseModel

class Product(BaseModel):
    code: int
    name: str
    productType: str
    total: float
    um: str




