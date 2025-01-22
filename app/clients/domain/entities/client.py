from app.clients.domain.value_objects.id import ID
from app.clients.domain.value_objects.dni import DNI
from app.clients.domain.value_objects.phone import Phone
from app.clients.domain.value_objects.email import Email
from app.clients.domain.value_objects.name import Name
from app.clients.domain.enums.frequency import Frequency
from app.clients.domain.enums.gender import Gender
from app.common.domain.entity import Entity

class Client(Entity):
    def __init__(self, id: ID, name: Name, dni: DNI, email: Email, frequency: Frequency, gender: Gender, phone: Phone):
        self.id = id
        self.name = name
        self.dni = dni
        self.email = email
        self.frequency = frequency
        self.gender = gender
        self.phone = phone

    @classmethod
    def create(cls, id: str, name: str, dni: str, email: str, frequency: str, gender: str, phone: str):
        id = ID.create(id)
        name = Name.create(name)
        dni = DNI.create(dni)
        email = Email.create(email)
        frequency = Frequency[frequency.upper()]
        gender = Gender[gender.upper()]
        phone = Phone.create(phone)
        return cls(id, name, dni, email, frequency, gender, phone)
    
    def update(self, name: str = None, dni: str = None, email: str = None, frequency: str = None, gender: str = None, phone: str = None):
        if name:
            self.name = Name.create(name)
        if email:
            self.email = Email.create(email)
        if dni:
            self.dni = DNI.create(dni)
        if frequency:
            self.frequency = Frequency[frequency.upper()]
        if gender:
            self.gender = Gender[gender.upper()]
        if phone:
            self.phone = Phone.create(phone)

    def get(self):
        return self

