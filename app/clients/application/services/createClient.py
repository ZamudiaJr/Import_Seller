from app.clients.domain.ports.IClientRepository import IClientRepository
from app.clients.application.dtos.createClientDto import CreateClientDto
from app.clients.domain.aggregates.client_aggregate import ClientAggregate
from uuid import uuid4

class CreateClientService:
    def __init__(self, repo: IClientRepository[ClientAggregate]):
        self.repo = repo

    async def execute(self, create_client_dto: CreateClientDto) -> None:
        client_aggregate = ClientAggregate.create(
            id=str(uuid4()),
            name=create_client_dto.name,
            dni=create_client_dto.dni,
            email=create_client_dto.email,
            frequency=create_client_dto.frequency,
            gender=create_client_dto.gender,
            phone=create_client_dto.phone
        )

        await self.repo.create_client(client_aggregate)
        return client_aggregate