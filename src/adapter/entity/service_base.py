from abc import ABC, abstractmethod

from src.schemas.entitys_schema import EntitysInput

class ServiceBase:
    
    @abstractmethod
    def find_by_id_entity(self, id:int):pass
    
    @abstractmethod
    def find_all_entity(self):pass
    
    @abstractmethod
    def create_entity(self, entitysInput:EntitysInput):pass
   
    @abstractmethod
    def update_entity(self, entitysInput:EntitysInput):pass
    
    @abstractmethod
    def delete_entity(self, id:int):pass