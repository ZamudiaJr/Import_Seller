from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ProductDto(BaseModel):
    id: UUID
    code: str
    type: str
    size: str
    gender: str
    price: float
    description: str