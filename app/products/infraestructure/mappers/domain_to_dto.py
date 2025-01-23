from app.products.domain.aggregate.product_aggregate import ProductAggregate
from app.products.application.dtos.productDto import ProductDto

def domain_to_dto(product_aggregate: ProductAggregate) -> ProductDto:
    return ProductDto(
        id=product_aggregate.product.id.get(),
        code=product_aggregate.product.code.get(),
        description=product_aggregate.product.description.get(),
        price=product_aggregate.product.price.get(),
        size=product_aggregate.product.size.get(),
        type=product_aggregate.product.type.value,
        gender=product_aggregate.product.gender.value
    )