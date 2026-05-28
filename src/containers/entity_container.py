from src.database.database_connection import DatabaseConnection
from src.repositories.entitys_repository import EntityRepository
from src.services.entity_service import EntityService
from src.controllers.entity_controller import EntityController

def entityContainer():
    
    database = DatabaseConnection()
    session = database.bootstrap()
    
    repository = EntityRepository(session())
    service = EntityService(repository)
    
    controller = EntityController(service)
    
    return controller
    
