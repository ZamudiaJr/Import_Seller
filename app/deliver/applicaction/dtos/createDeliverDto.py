from pydantic import BaseModel, Field
from datetime import date as fecha

class CreateDeliverDto(BaseModel):

    client_dni: str = Field(..., description="El dni del cliente a quien se le está asociando el entregable", example="12345678")
    state: str = Field(..., description="EL estado donde será entregado el pedido", example="Miranda or Zulia or Sucre")
    city: str = Field(..., description="La ciudad donde será entregado el pedido", example="Guatire")
    township: str = Field(..., description="El monucio donde seráentregado el pedido", example="Zamora")
    street: str = Field(..., description="La calle en donde será entregado el pedido", example="La Jarana")
    status: str = Field(..., description="El estado en el que se encuentra el pedido", example="Agencia or Rodando or Entregado")
    date: fecha = Field(..., description="ELa fecha en la que se hará entrega", example="2025-01-24")
    type: str = Field(..., description="La modalidad en la que se hará entrega del pedido", example="Nacional or Pick Up or Delivery")
    agency: str = Field(..., description="La agencia con la que será enviado el pedido", example="Zoom or MRW or Yummy or NA")