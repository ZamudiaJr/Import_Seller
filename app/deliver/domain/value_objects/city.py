from app.common.domain.value_object import ValueObject

class City(ValueObject):
    def __init__(self, city: str):
        self._city = city

    @classmethod
    def create(cls, city: str):
        return cls(city)

    def get(self) -> str:
        return self._city