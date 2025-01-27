from pydantic import BaseModel, Field
from datetime import date as fecha
from uuid import UUID

class DeliverDto(BaseModel):

    id: UUID
    state: str
    city: str
    township: str
    street: str
    status: str
    date: fecha
    type: str
    agency: str
    client_name: str
    client_dni: str