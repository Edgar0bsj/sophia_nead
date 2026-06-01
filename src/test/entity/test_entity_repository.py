import pytest

from src.database.database_connection import DatabaseConnection
from src.models.entitys_model import EntitysModel
from src.repositories.entitys_repository import EntityRepository

@pytest.fixture
def repository():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = EntityRepository(session())
    return repository
    
    
@pytest.fixture
def entity_model():
    return EntitysModel(
            sistema = "SOPHIA",
            unidade = "UNIG",
            entity_name = 'Campus',
            oldExternalId = '123456789',
            newExternalId = '987654321'
        )


class TestEntityRepository:

    
    def test_create(self, repository:EntityRepository, entity_model:EntitysModel):

        resultCreate = repository.save(entity_model)  
        
        assert isinstance(resultCreate, EntitysModel)
        assert resultCreate is not None

    def test_update(self, repository:EntityRepository, entity_model:EntitysModel):
        resultCreate = repository.save(entity_model) 
        
        resultCreate.sistema = "AVALIA"
        resultCreate.unidade = "UNIG"
        resultCreate.entity_name = "polo"
        resultCreate.oldExternalId = "741852963"
        resultCreate.newExternalId = "147258369"
        
        resultUpdate = repository.update(resultCreate)
        
        assert isinstance(resultUpdate, EntitysModel)
        assert resultCreate is not None
        assert resultUpdate.id == resultCreate.id
        assert resultUpdate.sistema == resultCreate.sistema
        assert resultUpdate.unidade == resultCreate.unidade
        assert resultUpdate.entity_name == resultCreate.entity_name
        assert resultUpdate.oldExternalId == resultCreate.oldExternalId
        assert resultUpdate.newExternalId == resultCreate.newExternalId
        
    def test_find_all(self, repository:EntityRepository):
        modalidadeAll = repository.find_all()
        
        assert modalidadeAll is not None
        assert isinstance(modalidadeAll, list)
        for i in modalidadeAll:
            assert isinstance(i, EntitysModel)

    def test_find_by_id(self, repository:EntityRepository, entity_model:EntitysModel):
        resultCreate = repository.save(entity_model)
        
        findId = repository.find_by_id(resultCreate.id)
        
        assert findId is not None
        assert findId == resultCreate

    def test_delete(self, repository:EntityRepository, entity_model:EntitysModel):
        modaCreated = repository.save(entity_model)
        
        resultDelete = repository.delete(modaCreated.id)
        
        deveSerNone = repository.find_by_id(resultDelete.id)
        
        assert deveSerNone is None
        assert resultDelete is not None
        assert resultDelete == modaCreated
        