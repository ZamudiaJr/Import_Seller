from app.products.domain.ports.IProductRepository import IProductRepository
from app.products.domain.aggregate.product_aggregate import ProductAggregate

class GetProductByCodeService:
    def __init__(self, repo: IProductRepository[ProductAggregate]):
        self.repo = repo

    async def get_product_by_code(self, product_code: str) -> ProductAggregate:
        product_aggregate = await self.repo.get_product_by_code(product_code)
        if not product_aggregate:
            raise ValueError(f"Product with code {product_code} not found")
        return product_aggregate