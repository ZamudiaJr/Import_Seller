from app.deliver.domain.ports.IDeliverRepository import IDeliverRepository
from app.deliver.domain.aggregate.delivery_aggregate import DeliverAggregate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.deliver.infraestructure.mappers.aggregate_to_model import aggregate_to_model
from app.deliver.infraestructure.mappers.model_to_domain import model_to_domain
from app.common.infraestructure.models import Entrega, Cliente

class DeliverRepository(IDeliverRepository[DeliverAggregate]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_deliver(self, deliver_aggregate: DeliverAggregate) -> None:
        deliver = aggregate_to_model(deliver_aggregate)
        self.session.add(deliver)
        await self.session.commit()
        await self.session.refresh(deliver)

    async def update_deliver(self, deliver_aggregate: DeliverAggregate) -> DeliverAggregate:
        deliver = aggregate_to_model(deliver_aggregate)
        await self.session.merge(deliver)
        await self.session.commit()

    async def get_deliver_by_id(self, deliver_id: str) -> DeliverAggregate:
        result = await self.session.execute(select(Entrega).where(Entrega.id == deliver_id))
        deliver_model = result.scalar_one_or_none()
        if deliver_model:
            result2 = await self.session.execute(select(Cliente).where(Cliente.id == deliver_model.cliente_id))
            client_model = result2.scalar_one_or_none()
            return model_to_domain(deliver_model, client_model)
        return None
    
    async def get_delivers_by_client_id(self, client_id: str) -> List[DeliverAggregate]:
        delivers_list = []
        result = await self.session.execute(select(Entrega).where(Entrega.cliente_id == client_id))
        deliver_models = result.scalars().all()
        for deliver_model in deliver_models:
            result2 = await self.session.execute(select(Cliente).where(Cliente.id == deliver_model.cliente_id))
            client_model = result2.scalar_one_or_none()
            delivers_list.append(model_to_domain(deliver_model, client_model))
        return [deliver for deliver in delivers_list]