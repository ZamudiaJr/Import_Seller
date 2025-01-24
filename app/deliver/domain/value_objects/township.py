from app.common.domain.value_object import ValueObject

#municipio
class Township(ValueObject):
    def __init__(self, township: str):
        self._township= township

    @classmethod
    def create(cls, township: str):
        return cls(township)

    def get(self) -> str:
        return self._township