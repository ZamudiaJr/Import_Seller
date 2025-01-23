from app.common.infraestructure.models import Producto
from app.products.domain.entities.product import Product
from app.products.domain.aggregate.product_aggregate import ProductAggregate
from app.products.domain.value_objects.id import ID
from app.products.domain.value_objects.code import Code
from app.products.domain.value_objects.description import Description
from app.products.domain.value_objects.price import Price
from app.products.domain.value_objects.size import Size
from app.products.domain.enums.gender import Gender
from app.products.domain.enums.type import Type

def model_to_domain(product_model: Producto) -> ProductAggregate:
    product = Product(
        id=ID(product_model.id),
        code=Code(product_model.codigo),
        description=Description(product_model.descripcion),
        price=Price(product_model.precio),
        size=Size(product_model.talla),
        gender=Gender(product_model.genero),
        type=Type(product_model.tipo_producto)
    )
    return ProductAggregate(id=ID(product_model.id), product=product)