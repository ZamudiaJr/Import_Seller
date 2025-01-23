from app.products.domain.ports.IProductRepository import IProductRepository
from app.products.domain.aggregate.product_aggregate import ProductAggregate
from app.products.application.dtos.updateProductDto import UpdateProductDto

class UpdateProductService:
    def __init__(self, repo: IProductRepository[ProductAggregate]):
        self.repo = repo

    async def updated_product(self, product_id: str, product_dto: UpdateProductDto) -> bool:
        product_aggregate = await self.repo.get_product_by_id(product_id)
        if not product_aggregate:
            raise ValueError(f"Product with id {product_id} not found")
        
        existing_products = await self.repo.get_products()
        for product in existing_products:
            if product.product.code.get() == product_dto.code and product.product.id != product_id:
                raise ValueError(f"Product with code {product_dto.code} already exists")
            
        product_aggregate.update(
            code=product_dto.code,
            description=product_dto.description,
            price=product_dto.price,
            size=product_dto.size,
            gender=product_dto.gender,
            type=product_dto.type
        )
        await self.repo.update_product(product_aggregate)
        return True