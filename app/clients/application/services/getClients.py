from app.clients.domain.ports.IClientRepository import IClientRepository
from app.clients.domain.aggregates.client_aggregate import ClientAggregate

class GetClientsService:
    def __init__(self, repo: IClientRepository[ClientAggregate]):
        self.repo = repo

    async def get_clients(self) -> list[ClientAggregate]:
        return await self.repo.get_clients()