from app.common.infraestructure.models import Entrega
from app.deliver.domain.aggregate.delivery_aggregate import DeliverAggregate

def aggregate_to_model(deliver_aggregate: DeliverAggregate) -> Entrega:
    return Entrega(
        id=deliver_aggregate.deliver.id.get(),
        estado=deliver_aggregate.deliver.street.get(),
        ciudad=deliver_aggregate.deliver.city.get(),
        municipio=deliver_aggregate.deliver.state.get(),
        calle=deliver_aggregate.deliver.street.get(),
        status=deliver_aggregate.deliver.status.value,
        fecha_entrega=deliver_aggregate.deliver.date.get(),
        tipo_entrega=deliver_aggregate.deliver.type.value,
        agencia=deliver_aggregate.deliver.agency.value,
        cliente_id=deliver_aggregate.client.id.get()
   )