from datetime import date
from app.common.domain.value_object import ValueObject

class Date(ValueObject):
    def __init__(self, date: date):
        self._date = date

    @classmethod
    def create(cls, date: date):
        return cls(date)

    def get(self) -> str:
        return self._date