from app.clients.domain.ports.IClientRepository import IClientRepository
from app.clients.domain.aggregates.client_aggregate import ClientAggregate

class DeleteClientService:
    def __init__(self, repo: IClientRepository[ClientAggregate]):
        self.repo = repo

    async def delete_client(self, client_id: str) -> None:
        client_aggregate = await self.repo.get_client_by_id(client_id)
        if not client_aggregate:
            raise ValueError(f"Client with id {client_id} not found")
        await self.repo.delete_client(client_id)