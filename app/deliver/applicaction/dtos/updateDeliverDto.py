from pydantic import BaseModel
from typing import Optional
from datetime import date as fecha

class UpdateDeliverDto(BaseModel):

    state: Optional[str] = None
    city: Optional[str] = None
    township: Optional[str] = None
    street: Optional[str] = None
    status: Optional[str] = None
    date: Optional[fecha] = None
    type: Optional[str] = None
    agency: Optional[str] = None