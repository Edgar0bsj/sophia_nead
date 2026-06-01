from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class ServiceInterface(ABC, Generic[T]):
    
    @abstractmethod
    def save(
        self,
        entity: T
    )-> T: ...
    
    @abstractmethod
    def update(
        self,
        entity: T
    )-> T: ...
    
    @abstractmethod
    def find_all(
        self
    )-> list[T]: ...
    
    @abstractmethod
    def find_by_id(
        self,
        id:int
    )-> Optional[T]: ...
    
    @abstractmethod
    def delete(
        self,
        id:int
    )-> Optional[T]: ...