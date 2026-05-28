from src.interface.entityInterface.entity_service_interface import EntityServiceInterface
from src.dto.entityDTO import EntityDTO
from src.models.entitys_model import EntitysModel

class EntityController:
    def __init__(
        self,
        service: EntityServiceInterface
        )-> None:
        self.service = service
        
    def create_entity(self, entity_dto:EntityDTO):
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