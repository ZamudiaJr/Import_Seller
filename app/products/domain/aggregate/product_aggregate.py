from app.products.domain.value_objects.id import ID
from app.products.domain.entities.product import Product
from app.common.domain.entity import Entity

class ProductAggregate(Entity):
    def __init__(self, id: ID, product: Product):
        self.id = id
        self.product = product

    @classmethod
    def create(cls, id: str, code: str, description: str, price: float, size: str, gender: str, type: str):
       product = Product.create(id, code, description, price, size, gender, type)
       return cls(id, product)

    def update(self, code: str = None, description: str = None, price: float = None, size: str = None, gender: str = None, type: str = None):
        self.product.update(code, description, price, size, gender, type)

    def get(self):
        return self.product 
        