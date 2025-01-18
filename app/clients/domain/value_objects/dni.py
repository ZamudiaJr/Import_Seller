from app.common.domain.value_object import ValueObject

class DNI(ValueObject):
    def __init__(self, dni: str):
        self._dni = dni
    
    @classmethod
    def create(cls, dni: str):
        return cls(dni)
        
    def get(self):
        return self._dni