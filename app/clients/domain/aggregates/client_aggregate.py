from app.clients.domain.value_objects.id import ID
from app.clients.domain.entities.client import Client
from app.common.domain.entity import Entity

class ClientAggregate(Entity):
    def __init__(self, id: ID, client: Client):
        self.id = id
        self.client = client

    @classmethod
    def create(cls, id: str, name: str, dni: str, email: str, frequency: str, gender: str):
        id = ID.create(id)
        client = Client.create(id, name, dni, email, frequency, gender)
        return cls(id, client)
    
    def update(self, name: str = None, dni: str = None, email: str = None, frequency: str = None, gender: str = None):
        self.client.update(name, dni, email, frequency, gender)

    def get(self):
        return self.client