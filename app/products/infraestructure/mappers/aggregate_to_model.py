from app.common.infraestructure.models import Producto
from app.products.domain.aggregate.product_aggregate import ProductAggregate

def aggregate_to_model(product_aggregate: ProductAggregate) -> Producto:
    return Producto(
        id=product_aggregate.product.id.get(),
        codigo=product_aggregate.product.code.get(),
        descripcion=product_aggregate.product.description.get(),
        precio=product_aggregate.product.price.get(),
        talla=product_aggregate.product.size.get(),
        genero=product_aggregate.product.gender.value,
        tipo_producto=product_aggregate.product.type.value
    )