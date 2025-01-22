from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod

T = TypeVar("T")

class IClientRepository(ABC, Generic[T]):
    
    @abstractmethod
    def create_client(self) -> None:
        pass

    @abstractmethod
    def update_client(self) -> None:
        pass

    @abstractmethod
    async def delete_client(self, id: int) -> None:
        pass

    @abstractmethod
    def get_clients(self) -> List[T]:
        pass

    @abstractmethod
    async def get_client_by_id(self, id: int) -> T:
        pass

    @abstractmethod
    async def get_client_by_dni(self, dni: str) -> T:
        pass

    