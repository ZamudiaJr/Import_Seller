from app.clients.domain.ports.IClientRepository import IClientRepository
from app.clients.domain.aggregates.client_aggregate import ClientAggregate

class GetClientByIdService:
    def __init__(self, repo: IClientRepository):
        self.repo = repo

    async def get_client_by_id(self, client_id: str) -> ClientAggregate:
        client_aggregate = await self.repo.get_client_by_id(client_id)
        if not client_aggregate:
            raise Exception(f"Client with id {client_id} not found")
        return client_aggregate