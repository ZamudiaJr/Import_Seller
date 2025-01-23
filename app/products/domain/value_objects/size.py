from app.common.domain.value_object import ValueObject

class Size(ValueObject):
    def __init__(self, size: str):
        self._size = size

    @classmethod
    def create(cls, size: str):
        return cls(size)

    def get(self) -> str:
        return self._size