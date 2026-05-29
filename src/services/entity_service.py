from src.interface.entityInterface.entity_service_interface import EntityServiceInterface
from src.models.entitys_model import EntitysModel
from src.interface.entityInterface.entity_repository_interface import EntityRepositoryInterface

from src.decorators.entityDecorators.service.upsert_decorator import UpsertDecorator

class EntityService(EntityServiceInterface[EntitysModel]):
    
    def __init__(self, entityRepository:EntityRepositoryInterface):
        self.repository = entityRepository
            
    def find_by_id_entity(self, id:int)-> EntitysModel:
        return (self.repository.find_by_id(id))
    
    def find_all_entity(self)-> list[EntitysModel]:
        return (self.repository.find_all())
    
    @UpsertDecorator
    def save_entity(self, entitysInput:EntitysModel)-> EntitysModel:
        return (self.repository.save(entitysInput))
    
    def update_entity(self, entitysInput:EntitysModel)-> EntitysModel:
        return (self.repository.update(entitysInput))
    
    def delete_entity(self, id:int)-> EntitysModel:
        return (self.repository.delete(id))