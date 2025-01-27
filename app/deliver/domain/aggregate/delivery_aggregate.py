from app.deliver.domain.entities.deliver import Deliver
from app.clients.domain.entities.client import Client
from app.deliver.domain.value_objects.id import ID
from app.common.domain.entity import Entity
from datetime import date

class DeliverAggregate(Entity):
    def __init__(self, id: ID, deliver: Deliver, client: Client):
        self.id = id
        self.deliver = deliver
        self.client = client

    @classmethod
    def create(cls, deliver_id: str, state: str, city: str, township: str, street: str, status: str, date: date, type: str, agency: str, client_id: str, name: str, dni: str, email: str, frequency: str, gender: str, phone: str):
        deliver = Deliver.create(deliver_id, state, city, township, street, status, date, type, agency)
        client = Client.create(client_id, name, dni, email, frequency, gender, phone)
        return cls(deliver_id, deliver, client)
    
    def update(self, state: str = None, city: str = None, township: str = None, street: str = None, status: str = None, date: date = None, type: str = None, agency: str = None):
        self.deliver.update(state, city, township, street, status, date, type, agency)

    def get(self):
        return self.deliver, self.client

