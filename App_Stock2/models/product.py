from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str = Field(..., max_length=30)
    code: Optional[int] = None
    stock: float = Field(...)
    typeProduct: str = Field(...)
    um: str = Field(...)