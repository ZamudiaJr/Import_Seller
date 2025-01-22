from app.common.infraestructure.models import Cliente
from app.clients.domain.aggregates.client_aggregate import ClientAggregate
from app.clients.domain.entities.client import Client
from app.clients.domain.value_objects.id import ID
from app.clients.domain.value_objects.dni import DNI
from app.clients.domain.value_objects.phone import Phone
from app.clients.domain.value_objects.email import Email
from app.clients.domain.value_objects.name import Name
from app.clients.domain.enums.frequency import Frequency
from app.clients.domain.enums.gender import Gender

def model_to_domain(client_model: Cliente) -> ClientAggregate:
    client = Client.create(
        id=ID.create(client_model.id),
        name=Name.create(client_model.nombre),
        dni=DNI.create(client_model.cedula),
        email=Email.create(client_model.correo),
        frequency=Frequency(client_model.frecuencia),
        gender=Gender(client_model.genero),
        phone=Phone.create(client_model.telefono)
    )

    return ClientAggregate(id=ID.create(client_model.id), client=client)