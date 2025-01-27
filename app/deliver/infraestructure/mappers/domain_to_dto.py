from app.deliver.domain.aggregate.delivery_aggregate import DeliverAggregate
from app.deliver.applicaction.dtos.deliverDto import DeliverDto

def domain_to_dto(deliver_aggregate: DeliverAggregate) -> DeliverDto:
    return DeliverDto(
        client_name=deliver_aggregate.client.name.get(),
        client_dni=deliver_aggregate.client.dni.get(),
        id=deliver_aggregate.deliver.id.get(),
        state=deliver_aggregate.deliver.state.get(),
        city=deliver_aggregate.deliver.city.get(),
        township=deliver_aggregate.deliver.township.get(),
        street=deliver_aggregate.deliver.street.get(),
        status=deliver_aggregate.deliver.status.value,
        date=deliver_aggregate.deliver.date.get(),
        type=deliver_aggregate.deliver.type.value,
        agency=deliver_aggregate.deliver.agency.value
    )