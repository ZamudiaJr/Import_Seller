from app.clients.domain.ports.IClientRepository import IClientRepository
from app.clients.domain.aggregates.client_aggregate import ClientAggregate

class GetClientByDNIService:
    def __init__(self, repo: IClientRepository):
        self.repo = repo

    async def get_client_by_dni(self, client_dni: str) -> ClientAggregate:
        client_aggregate = await self.repo.get_client_by_dni(client_dni)
        if not client_aggregate:
            raise Exception(f"Client with with {client_dni} not found")
        return client_aggregate