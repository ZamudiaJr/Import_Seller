from app.common.domain.value_object import ValueObject

class Street(ValueObject):
    def __init__(self, street: str):
        self._street = street

    @classmethod
    def create(cls, street: str):
        return cls(street)

    def get(self) -> str:
        return self._street