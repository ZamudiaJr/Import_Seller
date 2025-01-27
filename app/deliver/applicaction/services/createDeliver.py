from app.deliver.domain.ports.IDeliverRepository import IDeliverRepository
from app.deliver.applicaction.dtos.createDeliverDto import CreateDeliverDto
from app.deliver.domain.aggregate.delivery_aggregate import DeliverAggregate
from app.clients.domain.aggregates.client_aggregate import ClientAggregate
from uuid import uuid4

class CreateDeliverService:
    def __init__(self, repo: IDeliverRepository[DeliverAggregate]):
        self.repo = repo

    async def create_deliver(self, deliver_dto: CreateDeliverDto, client_aggregate: ClientAggregate) -> DeliverAggregate:

        deliver_aggregate = DeliverAggregate.create(
            deliver_id=str(uuid4()),
            state=deliver_dto.state,
            city=deliver_dto.city,
            township=deliver_dto.township,
            street=deliver_dto.street,
            status=deliver_dto.status,
            date=deliver_dto.date,
            type=deliver_dto.type,
            agency=deliver_dto.agency,
            client_id=client_aggregate.id.get(),
            name=client_aggregate.client.name.get(),
            dni=client_aggregate.client.dni.get(),
            email=client_aggregate.client.email.get(),
            frequency=client_aggregate.client.frequency.value,
            gender=client_aggregate.client.gender.value,
            phone=client_aggregate.client.phone.get()
        )

        await self.repo.create_deliver(deliver_aggregate)
        return deliver_aggregate
