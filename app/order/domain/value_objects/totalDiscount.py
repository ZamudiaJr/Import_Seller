from app.common.domain.value_object import ValueObject

class TotalDiscount(ValueObject):
    def __init__(self, totalDiscount: float):
        self._totalDiscount = totalDiscount

    @classmethod
    def create(cls, totalDiscount: float):
        return cls(totalDiscount)

    def get(self) -> float:
        return self._totalDiscount