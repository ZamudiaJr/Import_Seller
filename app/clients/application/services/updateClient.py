from app.clients.domain.ports.IClientRepository import IClientRepository
from app.clients.domain.aggregates.client_aggregate import ClientAggregate
from app.clients.application.dtos.updateClientDto import UpdateClientDto

class UpdateClientService:
    def __init__(self, repo: IClientRepository[ClientAggregate]) -> bool:
        self.repo = repo

    async def update_client(self, client_id: str, client_update_dto: UpdateClientDto) -> ClientAggregate:
        client_aggregate = await self.repo.get_client_by_id(client_id)
        if not client_aggregate:
            raise ValueError(f"Client with id {client_id} not found")
        
        client_aggregate.update(
            name=client_update_dto.name,
            dni=client_update_dto.dni,
            email=client_update_dto.email,
            phone=client_update_dto.phone,
            frequency=client_update_dto.frequency,
        )
        
        await self.repo.update_client(client_aggregate)
        return True