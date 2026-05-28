from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")

class EntityServiceInterface(ABC, Generic[T]):
    
    @abstractmethod
    def save_entity(
        self,
        entity: T
    )-> T: ...
    
    @abstractmethod
    def update_entity(
        self,
        entity: T
    )-> T: ...
    
    @abstractmethod
    def find_all_entity(
        self
    )-> list[T]: ...
    
    @abstractmethod
    def find_by_id_entity(
        self,
        id:int
    )-> T: ...
    
    @abstractmethod
    def delete_entity(
        self,
        id:int
    )-> T: ...