from app.clients.domain.aggregates.client_aggregate import ClientAggregate
from app.clients.application.dtos.clientDto import ClientDto

def domain_to_dto(client_aggregate: ClientAggregate) -> ClientDto:
    client = client_aggregate.get()
    return ClientDto(
        id=client_aggregate.id.get(),
        name=client.name.get(),
        dni=client.dni.get(),
        email=client.email.get(),
        frequency=client.frequency.value,
        gender=client.gender.value,
        phone=client.phone.get()
    )