from pydantic import BaseModel

class ClientDto(BaseModel):
    id: int
    dni: str
    name: str
    phone: str
    email: str
    frequency: str
    gender: str