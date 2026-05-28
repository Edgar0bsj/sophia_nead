from src.interface.entityInterface.entity_service_interface import EntityServiceInterface
from src.dto.entityDTO import EntityDTO
from src.models.entitys_model import EntitysModel

class EntityController:
    def __init__(
        self,
        service: EntityServiceInterface
        )-> None:
        self.service = service
        
    def create_entity(self, entity_dto:EntityDTO)-> EntitysModel:
        try:
            entity = EntitysModel(
                sistema= entity_dto.sistema,
                unidade= entity_dto.unidade,
                entity_name= entity_dto.entity_name,
                oldExternalId= entity_dto.oldExternalId,
                newExternalId= entity_dto.newExternalId,
            )
            return self.service.save_entity(entity)
        
        except Exception as err:
            print(err)
        
    def find_all_entity(self)-> list[EntitysModel]:
        try:
            return (self.service.find_all_entity())
        except Exception as err:
            print(err)
            raise
        
    def find_by_id_entity(self, id:int):
        try:
            return (self.service.find_by_id_entity(id))
        except Exception as err:
            print(err)
            raise
        
    def update_entity(self, entityModel:EntitysModel)-> EntitysModel:
        try:
            return (self.service.update_entity(entityModel))
        except Exception as err:
            print(err)
            raise
    
    def remove_entity(self, id:int):
        try:
            return (self.service.delete_entity(id))
        except Exception as err:
            print(err)
            raise