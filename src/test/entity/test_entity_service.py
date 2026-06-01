import pytest

from src.models.entitys_model import EntitysModel
from src.database.database_connection import DatabaseConnection

from src.services.entity_service import EntityService
from src.repositories.entitys_repository import EntityRepository


@pytest.fixture
def service():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = EntityRepository(session())

    service = EntityService(repository)
    return service


@pytest.fixture
def entity_model():
    return EntitysModel(
        sistema="SOPHIA",
        unidade="UNIG",
        entity_name="Campus",
        oldExternalId="123456789",
        newExternalId="987654321",
    )


class TestEntityService:

    def test_save(
        self, service: EntityService, entity_model: EntitysModel
    ) -> EntitysModel:
        result = service.save(entity_model)

        assert result.newExternalId == entity_model.newExternalId
        assert result is not None
        assert isinstance(result, EntitysModel)

    def test_update(
        self, service: EntityService, entity_model: EntitysModel
    ) -> EntitysModel:
        entityCreated = service.save(entity_model)

        entityCreated.sistema = "AVALIA"
        entityCreated.unidade = "ITAPERUNA"
        entityCreated.entity_name = "polo"
        entityCreated.oldExternalId = "1112223344"
        entityCreated.newExternalId = "6655443322"

        result = service.update(entityCreated)

        assert result.id == entityCreated.id
        assert result is not None
        assert isinstance(result, EntitysModel)

    def test_find_by_id(
        self, service: EntityService, entity_model: EntitysModel
    ) -> EntitysModel:
        created = service.save(entity_model)

        findResult = service.find_by_id(created.id)

        assert findResult is not None
        assert isinstance(findResult, EntitysModel)
        assert findResult.id == created.id

    def test_find_all(self, service: EntityService):
        result = service.find_all()

        assert result is not None
        assert isinstance(result, list)
        if len(result) > 0:
            for i in result:
                assert isinstance(i, EntitysModel)

    def test_delete(
        self, service: EntityService, entity_model: EntitysModel
    ) -> EntitysModel:
        created = service.save(entity_model)

        result = service.delete(created.id)

        deveSerNone = service.find_by_id(created.id)

        assert result is not None
        assert isinstance(result, EntitysModel)
        assert deveSerNone is None

    def test_update_insert_entity(self, service: EntityService):
        entity_1 = EntitysModel(
            sistema="TESTE",
            unidade="TESTEE",
            entity_name="campusS",
            oldExternalId="123456789",
            newExternalId="987654321",
        )

        created_entity_1 = service.save(entity_1)

        entity_2 = EntitysModel(
            sistema="TESTE",
            unidade="TESTEE",
            entity_name="campusS",
            oldExternalId="999999999",
            newExternalId="888888888",
        )

        created_entity_2 = service.save(entity_2)

        entity_1_output = service.find_by_id(created_entity_1.id)
        entity_2_output = service.find_by_id(created_entity_2.id)

        assert isinstance(entity_1_output, EntitysModel)
        assert isinstance(entity_2_output, EntitysModel)
        assert entity_1_output.id == entity_2_output.id
