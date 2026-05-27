from src.repositories.entitys_repository import EntityRepository
from src.services.entity_service import EntityService



class EntityContainer:
    
    @staticmethod
    def create():
        repository = EntityRepository()
        service = EntityService(repository)
        
        
        return service