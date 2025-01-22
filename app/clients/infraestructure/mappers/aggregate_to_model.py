from app.common.infraestructure.models import Cliente
from app.clients.domain.aggregates.client_aggregate import ClientAggregate

def aggregate_to_model(client_aggregate: ClientAggregate) -> Cliente:
    return Cliente(
        id=client_aggregate.client.id.get(),
        name=client_aggregate.client.name.get(),
        dni=client_aggregate.client.dni.get(),
        email=client_aggregate.client.email.get(),
        frequency=client_aggregate.client.frequency.value,
        gender=client_aggregate.client.gender.value,
        phone=client_aggregate.client.phone.get()
    )
