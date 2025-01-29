from app.deliver.domain.ports.IDeliverRepository import IDeliverRepository
from app.deliver.domain.aggregate.delivery_aggregate import DeliverAggregate
from app.deliver.applicaction.dtos.updateDeliverDto import UpdateDeliverDto

class UpdateDeliverService:
    def __init__(self, repo: IDeliverRepository[DeliverAggregate]):
        self.repo = repo

    async def update_deliver(self, deliver_id: str, deliver_dto = UpdateDeliverDto) -> bool:
        deliver_aggregate = await self.repo.get_deliver_by_id(deliver_id)
        if not deliver_aggregate:
            raise ValueError(f"Deliver with id {deliver_id} not found")
        
        deliver_aggregate.update(
            state=deliver_dto.state,
            city=deliver_dto.city,
            township=deliver_dto.township,
            street=deliver_dto.street,
            status=deliver_dto.status,
            date=deliver_dto.date,
            type=deliver_dto.type,
            agency=deliver_dto.agency
        )

        await self.repo.update_deliver(deliver_aggregate)
        return True