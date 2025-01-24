from app.common.domain.entity import Entity
from app.deliver.domain.value_objects.id import ID
from app.deliver.domain.value_objects.date import Date
from app.deliver.domain.value_objects.state import State
from app.deliver.domain.value_objects.street import Street
from app.deliver.domain.value_objects.township import Township
from app.deliver.domain.value_objects.city import City
from app.deliver.domain.enums.agency import Agency
from app.deliver.domain.enums.status import Status
from app.deliver.domain.enums.type import Type
from datetime import date

class Deliver(Entity):
    def __init__(self, id: ID, state: State, city: City, township: Township, street: Street, status: Status, date: Date, type: Type, agency: Agency):
        self.id = id
        self.state = state
        self.city = city
        self.township = township
        self.street = street
        self.status = status
        self.date = date
        self.type = type
        self.agency = agency

    @classmethod
    def create(cls, id: str, state: str, city: str, township: str, street: str, status: str, date: date, type: str, agency: str):
        id = ID.create(id)
        state = State.create(state)
        city = City.create(city)
        township = Township.create(township)
        street = Street.create(street)
        status = Status[status.upper()]
        date = Date.create(date)
        type = Type[type.upper()]
        agency = Agency[agency.upper()]
        return cls(id, state, city, township, street, status, date, type, agency)
    
    def update(self, state: str = None, city: str = None, township: str = None, street: str = None, status: str = None, date: date = None, type: str = None, agency: str = None):
        if state:
            self.state = State.create(state)
        if city:
            self.city = City.create(city)
        if township:
            self.township = Township.create(township)
        if street:
            self.street = Street.create(street)
        if status:
            self.status = Status[status.upper()]
        if date:
            self.date = Date.create(date)
        if type:
            self.type = Type[type.upper()]
        if agency:
            self.agency = Agency[agency.upper()]

    def get(self):
        return self