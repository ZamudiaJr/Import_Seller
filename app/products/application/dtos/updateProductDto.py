from pydantic import BaseModel
from typing import Optional

class UpdateProductDto(BaseModel):
    code: Optional[str] = None
    type: Optional[str] = None
    size: Optional[str] = None
    gender: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None