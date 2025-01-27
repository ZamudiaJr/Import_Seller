from datetime import date
from typing import Optional
from enum import Enum
from sqlmodel import SQLModel, Relationship, Field, UniqueConstraint
from uuid import uuid4

class BasePedido (SQLModel):
    tienda: str
    total: float
    fecha_compra: date
    descuento: bool
    monto_desc: Optional[float] = None

class Pedido(BasePedido, table=True):
    __tablename__ = "pedidos"
    id: str = Field(default_factory= lambda: str(uuid4()), primary_key=True)
    detalles_pedido: list["DetallePedido"] = Relationship(back_populates="pedido")
    entrega_id: int = Field(foreign_key="entregas.id")
    entrega: "Entrega" = Relationship(back_populates="pedido")

class BaseProducto(SQLModel):
    codigo: str = Field(unique=True)
    tipo_producto: str
    talla: Optional[int] = None
    genero: str
    precio: float
    descripcion: str

class Producto(BaseProducto, table=True):
    __tablename__ = "productos"
    id: str = Field(default_factory= lambda: str(uuid4()), primary_key=True)
    detalles_pedido: list["DetallePedido"] = Relationship(back_populates="producto")

class BaseDetallePedido(SQLModel):
    cantidad: int

class DetallePedido(BaseDetallePedido, table=True):
    __table_args__ = (
        UniqueConstraint("pedido_id", "producto_id", name="unique_pedido_producto"),
    )
    id: str = Field(default_factory= lambda: str(uuid4()), primary_key=True)
    pedido_id: int = Field(foreign_key="pedidos.id")
    pedido: Pedido = Relationship(back_populates="detalles_pedido")
    producto_id: int = Field(foreign_key="productos.id")
    producto: Producto = Relationship(back_populates="detalles_pedido")

class baseCliente(SQLModel):
    cedula: str
    nombre: str
    telefono: str
    correo: str
    frecuencia: str# = Field(sa_column=Column(Enum(tipoFrecuencia)))
    genero: str #tipoGenero = Field(sa_column=Column(Enum(tipoGenero)))
    
class Cliente(baseCliente, table=True):
    __tablename__ = "clientes"
    id: str = Field(default_factory= lambda: str(uuid4()), primary_key=True)
    entregas: list["Entrega"] = Relationship(back_populates="cliente")

class baseEntrega(SQLModel):
    estado: str
    ciudad: str
    municipio: str
    calle: str
    status: str
    fecha_entrega: Optional[date] = None
    tipo_entrega: str
    agencia: str

class Entrega(baseEntrega, table=True):
    __tablename__ = "entregas"
    id: str = Field(default_factory= lambda: str(uuid4()), primary_key=True)
    cliente_id: int = Field(foreign_key="clientes.id")
    cliente: Cliente = Relationship(back_populates="entregas")
    pedido: list[Pedido] = Relationship(back_populates="entrega")
    
