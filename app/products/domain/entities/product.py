from app.products.domain.value_objects.code import Code
from app.products.domain.value_objects.description import Description
from app.products.domain.value_objects.price import Price
from app.products.domain.value_objects.size import Size
from app.products.domain.value_objects.id import ID
from app.products.domain.enums.gender import Gender
from app.products.domain.enums.type import Type
from app.common.domain.entity import Entity

class Product(Entity):
    def __init__(self, id: ID, code: Code, description: Description, price: Price, size: Size, gender: Gender, type: Type):
        self.id = id
        self.code = code
        self.description = description
        self.price = price
        self.size = size
        self.gender = gender
        self.type = type

    @classmethod
    def create(cls, id: str, code: str, description: str, price: float, size: str, gender: str, type: str):
        id = ID.create(id)
        code = Code.create(code)
        description = Description.create(description)
        price = Price.create(price)
        size = Size.create(size)
        gender = Gender[gender.upper()]
        type = Type[type.upper()]
        return cls(id, code, description, price, size, gender, type)
    
    def update(self, code: str = None, description: str = None, price: float = None, size: str = None, gender: str = None, type: str = None):
        if code:
            self.code = Code.create(code)
        if description:
            self.description = Description.create(description)
        if price:
            self.price = Price.create(price)
        if size:
            self.size = Size.create(size)
        if gender:
            self.gender = Gender[gender.upper()]
        if type:
            self.type = Type[type.upper()]

    def get(self):
        return self
