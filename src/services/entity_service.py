from src.adapter.entity.repository_base import RepositoryBase
from src.schemas.entitys_schema import EntitysInput

class EntityService:
    
    def __init__(self, entityRepository:RepositoryBase):
        self.repository = entityRepository
            
    def find_by_id_entity(self, id:int):
        return (self.repository.find_by_id(id))
    
    def find_all_entity(self):
        return (self.repository.find_all())
    
    def create_entity(self, entitysInput:EntitysInput):
        return (self.repository.create(entitysInput))
    
    def update_entity(self, entitysInput:EntitysInput):
        return (self.repository.update(entitysInput))
    
    def delete_entity(self, id:int):
        return (self.repository.delete(id))