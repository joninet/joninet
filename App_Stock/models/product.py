from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional [int] = None
    name: str = Field(..., max_length=30)
    code: int = Field(...,)
    stock: float = Field(...)
    typeProduct: str = Field(...)
    um: str = Field(...)