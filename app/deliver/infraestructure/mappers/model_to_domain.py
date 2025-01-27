from app.common.infraestructure.models import Entrega, Cliente
from app.deliver.domain.aggregate.delivery_aggregate import DeliverAggregate
from app.deliver.domain.value_objects.id import ID as DeliverID
from app.deliver.domain.value_objects.date import Date
from app.deliver.domain.value_objects.state import State
from app.deliver.domain.value_objects.street import Street
from app.deliver.domain.value_objects.township import Township
from app.deliver.domain.value_objects.city import City
from app.deliver.domain.enums.agency import Agency
from app.deliver.domain.enums.status import Status
from app.deliver.domain.enums.type import Type
from app.clients.domain.value_objects.id import ID as ClientID
from app.clients.domain.value_objects.dni import DNI
from app.clients.domain.value_objects.phone import Phone
from app.clients.domain.value_objects.email import Email
from app.clients.domain.value_objects.name import Name
from app.clients.domain.enums.frequency import Frequency
from app.clients.domain.enums.gender import Gender
from app.deliver.domain.entities.deliver import Deliver
from app.clients.domain.entities.client import Client

def model_to_domain(entrega_model: Entrega, cliente_model: Cliente) -> DeliverAggregate:
    deliver = Deliver(
        DeliverID.create(entrega_model.id),
        State.create(entrega_model.estado),
        City.create(entrega_model.ciudad),
        Township.create(entrega_model.municipio),
        Street.create(entrega_model.calle),
        Status(entrega_model.status),
        Date.create(entrega_model.fecha_entrega),
        Type(entrega_model.tipo_entrega),
        Agency(entrega_model.agencia)
    )
    client = Client(
        ClientID.create(cliente_model.id),
        Name.create(cliente_model.nombre),
        DNI.create(cliente_model.cedula),
        Email.create(cliente_model.correo),
        Frequency(cliente_model.frecuencia),
        Gender(cliente_model.genero),
        Phone.create(cliente_model.telefono)
    )
    return DeliverAggregate(id=DeliverID(entrega_model.id), deliver=deliver, client=client)