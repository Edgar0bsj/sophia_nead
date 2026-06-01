from src.interface.service_interface import ServiceInterface
from src.models.entitys_model import EntitysModel
from src.interface.repository_interface import RepositoryInterface

from src.decorators.entityDecorators.service.upsert_decorator import UpsertDecorator

class EntityService(ServiceInterface[EntitysModel]):
    
    def __init__(self, entityRepository:RepositoryInterface):
        self.repository = entityRepository
            
    def find_by_id(self, id:int)-> EntitysModel:
        return (self.repository.find_by_id(id))
    
    def find_all(self)-> list[EntitysModel]:
        return (self.repository.find_all())
    
    @UpsertDecorator
    def save(self, entitysInput:EntitysModel)-> EntitysModel:
        return (self.repository.save(entitysInput))
    
    def update(self, entitysInput:EntitysModel)-> EntitysModel:
        return (self.repository.update(entitysInput))
    
    def delete(self, id:int)-> EntitysModel:
        return (self.repository.delete(id))