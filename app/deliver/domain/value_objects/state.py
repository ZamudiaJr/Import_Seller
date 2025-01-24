from app.common.domain.value_object import ValueObject

class State(ValueObject):
    def __init__(self, state: str):
        self._state = state

    @classmethod
    def create(cls, state: str):
        return cls(state)

    def get(self) -> str:
        return self._state