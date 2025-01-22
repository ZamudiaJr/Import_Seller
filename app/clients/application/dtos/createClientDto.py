from pydantic import BaseModel, Field, field_validator
import re

class CreateClientDto(BaseModel):
    dni: str = Field(..., description="DNI of the client", example="12345678")
    name: str = Field(..., description="Name of the client", example="Juan Perez")
    phone: str = Field(..., description="Phone of the client", example="0414-3985096")
    email: str = Field(..., description="Email of the client", example="correo@gmail.com")
    frequency: str = Field(..., description="Frequency of the client", example="Semanal or Mensual or Trimestral or Semestral or Anual")
    gender: str = Field(..., description="Gender of the client", example="Masculino or Femenino")

    @field_validator('email')
    def validate_email(cls, value):
        if value is None or value == "":
            raise ValueError('Email is rrequired.')
        # Expresión regular para validar el formato del correo electrónico
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, value):
            raise ValueError('Invalid email format.')
        return value