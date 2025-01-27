from app.deliver.domain.ports.IDeliverRepository import IDeliverRepository
from app.deliver.domain.aggregate.delivery_aggregate import DeliverAggregate

class GetDeliverByClientIdService:
    def __init__(self, repo: IDeliverRepository[DeliverAggregate]):
        self.repo = repo

    async def get_deliver_by_client_id(self, client_id: str) -> DeliverAggregate:
        return await self.repo.get_delivers_by_client_id(client_id)