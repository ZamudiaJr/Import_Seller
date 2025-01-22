from app.common.domain.value_object import ValueObject

class Phone(ValueObject):
    def __init__(self, phone: str):
        self._phone = phone
    
    @classmethod
    def create(cls, phone: str):
        return cls(phone)
        
    
    def get(self):
        return self._phone