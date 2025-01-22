from pydantic import BaseModel

class ClientDto(BaseModel):
    id: str
    dni: str
    name: str
    phone: str
    email: str
    frequency: str
    gender: str