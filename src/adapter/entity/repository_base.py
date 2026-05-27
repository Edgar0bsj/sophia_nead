from abc import ABC, abstractmethod

from src.models.entitys_model import EntitysModel
from src.schemas.entitys_schema import EntitysInput

class RepositoryBase(ABC):
    
    @abstractmethod
    def find_all(self)-> list[EntitysModel]: pass
    
    @abstractmethod
    def find_by_id(self, entity_id:int)-> EntitysModel: pass
    
    @abstractmethod
    def create(self, entityInput:EntitysInput)-> EntitysInput: pass
    
    @abstractmethod
    def update(self, entityInput:EntitysInput)-> EntitysInput: pass
    
    @abstractmethod
    def delete(self, id:int)-> EntitysModel: pass