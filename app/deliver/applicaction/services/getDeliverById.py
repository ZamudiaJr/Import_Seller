from app.deliver.domain.ports.IDeliverRepository import IDeliverRepository
from app.deliver.domain.aggregate.delivery_aggregate import DeliverAggregate

class GetDeliverById:
    def __init__(self, repo: IDeliverRepository[DeliverAggregate]):
        self.repo = repo

    async def get_deliver_by_id(self, deliver_id: str) -> DeliverAggregate:
        deliver_aggregate = await self.repo.get_deliver_by_id(deliver_id)
        if not deliver_aggregate:
            raise ValueError(f"Deliver with id {deliver_id} not found")
        return deliver_aggregate