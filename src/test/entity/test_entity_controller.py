import pytest

from src.models.entitys_model import EntitysModel
from src.database.database_connection import DatabaseConnection

from src.services.entity_service import EntityService
from src.repositories.entitys_repository import EntityRepository
from src.controllers.entity_controller import EntityController


@pytest.fixture
def controller():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = EntityRepository(session())

    service = EntityService(repository)
    controller = EntityController(service)
    return controller


@pytest.fixture
def entity_model():
    return EntitysModel(
        sistema="SOPHIA",
        unidade="ITAPERUNA",
        entity_name="Campus",
        oldExternalId="123456789",
        newExternalId="987654321",
    )


class TestEntityService:

    def test_create_entity(
        self, controller: EntityController, entity_model: EntitysModel
    ):
        created = controller.create_entity(entity_model)

        assert created is not None
        assert isinstance(created, EntitysModel)

    def test_update_entity(
        self, controller: EntityController, entity_model: EntitysModel
    ):
        created = controller.create_entity(entity_model)

        created.entity_name = "buzios"

        result = controller.update_entity(created)

        assert result is not None
        assert isinstance(result, EntitysModel)
        assert result.id == created.id
        assert result.entity_name == created.entity_name

    def test_find_all_entity(self, controller: EntityController):
        result = controller.find_all_entity()

        assert result is not None
        assert isinstance(result, list)
        for i in result:
            assert isinstance(i, EntitysModel)

    def test_find_by_id_entity(
        self, controller: EntityController, entity_model: EntitysModel
    ):

        created = controller.create_entity(entity_model)

        resultFind = controller.find_by_id_entity(created.id)

        assert resultFind.id == created.id
        assert isinstance(resultFind, EntitysModel)
        assert resultFind is not None

    def test_remove_entity(
        self, controller: EntityController, entity_model: EntitysModel
    ):
        created = controller.create_entity(entity_model)

        removeResult = controller.remove_entity(created.id)

        assert removeResult is not None
        assert isinstance(removeResult, EntitysModel)
        assert removeResult.id == created.id
