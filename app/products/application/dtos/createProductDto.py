from pydantic import BaseModel, Field
from typing import Optional

class CreateProductDto(BaseModel):
    code: str = Field(..., description="Product code in its respective store", example="asd4-asd455-asss")
    type: str = Field(..., description="Type of product", example="Zapatos or Chaqueta or Lentes or Lenceria or Accesorios or Productos hogar")
    size: str = Field(..., description="Size of the product", example="S, M, L, XL, 6, 7, 8, 9, 10")
    gender: str = Field(..., description="Gender of the product", example="Masculino or Femenino")
    price: float = Field(..., description="Price of the product in its respective store", example=100.00)
    description: str = Field(..., description="Description of the product and the name of the Store", example="Este producto es de Shein")