from app.common.infraestructure.models import Cliente
from app.clients.domain.aggregates.client_aggregate import ClientAggregate

def aggregate_to_model(client_aggregate: ClientAggregate) -> Cliente:
    return Cliente(
        id=client_aggregate.id.get(),
        nombre=client_aggregate.client.name.get(),
        cedula=client_aggregate.client.dni.get(),
        correo=client_aggregate.client.email.get(),
        frecuencia=client_aggregate.client.frequency.value,
        genero=client_aggregate.client.gender.value,
        telefono=client_aggregate.client.phone.get()
    )

