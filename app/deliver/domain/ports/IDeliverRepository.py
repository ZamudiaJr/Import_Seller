from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod

T = TypeVar('T')

class IDeliverRepository(ABC, Generic[T]):

    @abstractmethod
    async def create_deliver(self) -> None:
        pass

    @abstractmethod
    async def update_deliver(self) -> None:
        pass

    @abstractmethod
    async def get_deliver_by_id(self, deliver_id: str) -> T:
        pass
    
    @abstractmethod
    async def get_delivers_by_client_id(self, client_id: str) -> List[T]:
        pass