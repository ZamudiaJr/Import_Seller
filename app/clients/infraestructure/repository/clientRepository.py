from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.common.infraestructure.models import Cliente
from app.clients.domain.ports.IClientRepository import IClientRepository
from app.clients.domain.aggregates.client_aggregate import ClientAggregate
from app.clients.infraestructure.mappers.aggregate_to_model import aggregate_to_model
from app.clients.infraestructure.mappers.model_to_domain import model_to_domain

class ClientRepository(IClientRepository[ClientAggregate]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_client(self, client_aggregate: ClientAggregate) -> None:
        client_model = aggregate_to_model(client_aggregate)
        print("RELEVANTEEEE")
        print(client_model.id)
        print(client_model.nombre)
        self.session.add(client_model)
        await self.session.commit()
        #await self.session.refresh(client_model)

    async def delete_client(self, client_id: str) -> None:
        result = await self.session.execute(select(Cliente).where(Cliente.id == client_id))
        client_model = result.scalar_one_or_none()
        if client_model:
            await self.session.delete(client_model)
            await self.session.commit()

    async def get_client_by_id(self, client_id: str) -> ClientAggregate:
        result = await self.session.execute(select(Cliente).where(Cliente.id == client_id))
        client_model = result.scalar_one_or_none()
        if client_model:
            return model_to_domain(client_model)
        return None
    
    async def get_client_by_dni(self, client_dni: str) -> ClientAggregate:
        result = await self.session.execute(select(Cliente).where(Cliente.cedula == client_dni))
        client_model = result.scalar_one_or_none()
        if client_model:
            return model_to_domain(client_model)
        return None

    async def get_clients(self) -> List[ClientAggregate]:
        result = await self.session.execute(select(Cliente))
        clients = result.scalars().all()
        return [model_to_domain(client) for client in clients]

    async def update_client(self, client_aggregate: ClientAggregate) -> None:
        client_model = aggregate_to_model(client_aggregate)
        await self.session.merge(client_model)
        await self.session.commit()
        return client_aggregate