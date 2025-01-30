from app.common.domain.value_object import ValueObject

class Discount(ValueObject):
    def __init__(self, discount: bool):
        self._discount = discount

    @classmethod
    def create(cls, discount: bool):
        return cls(discount)

    def get(self) -> bool:
        return self._discount