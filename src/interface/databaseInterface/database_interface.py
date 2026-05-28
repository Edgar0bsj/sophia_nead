from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class DataBaseInterface(ABC, Generic[T]):
        
    @abstractmethod
    def bootstrap(
        self
    )-> T: ...