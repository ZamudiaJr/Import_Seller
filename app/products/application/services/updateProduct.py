from app.products.domain.ports.IProductRepository import IProductRepository
from app.products.application.dtos.createProductDto import CreateProductDto
from app.products.domain.aggregate.product_aggregate import ProductAggregate
from uuid import uuid4

class CreateProductService:
    def __init__(self, repo: IProductRepository[ProductAggregate]):
        self.repo = repo

    async def create_product(self, product_dto: CreateProductDto):
        
        existing_products = await self.repo.get_products()
        for product in existing_products:
            if product.product.code.get() == product_dto.code:
                raise ValueError(f"Product with code {product_dto.code} already exists")

        product_aggregate = ProductAggregate.create(
            id = str(uuid4()), 
            code = product_dto.code,
            description = product_dto.description,
            price = product_dto.price,
            size = product_dto.size,
            gender=product_dto.gender,
            type=product_dto.type
        )

        await self.repo.create_product(product_aggregate)
        return product_aggregate