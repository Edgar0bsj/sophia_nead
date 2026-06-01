from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class RepositoryInterface(ABC, Generic[T]):
    
    @abstractmethod
    def save(
        self,
        entity: T
    ) -> T: ...
    
    @abstractmethod
    def find_by_id(
        self,
        id:int
    )-> Optional[T]: ...
    
    @abstractmethod
    def find_all(
        self
    )-> list[T]: ...
    
    @abstractmethod
    def update(
        self,
        entity: T
    )-> T: ...
    
    @abstractmethod
    def delete(
        self,
        id: int
    )-> Optional[T]: ...