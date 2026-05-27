from src.models.entitys_model import EntitysModel
from src.database.tables import Tables
from src.containers.entity_container import EntityContainer
from src.schemas.entitys_schema import EntitysInput


class TestEntityService:

    def setup_method(self):

        Tables().create_tables()

        self.entityService = EntityContainer.create()

    def test_find_all_entity(self):

        result = self.entityService.find_all_entity()

        assert isinstance(result, list)

        assert all(
            isinstance(item, EntitysModel)
            for item in result
        )

    def test_create_entity(self):

        entityInput = EntitysInput(
            sistema="Sophia",
            entity_name="campus",
            unidade="Unig",
            oldExternalId="123456",
            newExternalId="654321"
        )

        result = self.entityService.create_entity(entityInput)

        assert isinstance(result, EntitysModel)

        assert result.id is not None

        assert result.entity_name == "campus"

    def test_find_by_id_entity(self):

        entityInput = EntitysInput(
            sistema="Sophia",
            entity_name="campus",
            unidade="Unig",
            oldExternalId="123456",
            newExternalId="654321"
        )

        created = self.entityService.create_entity(
            entityInput
        )

        result = self.entityService.find_by_id_entity(
            created.id
        )

        assert isinstance(result, EntitysModel)

        assert result.id == created.id

    def test_update_entity(self):

        entityInput = EntitysInput(
            sistema="Sophia",
            entity_name="campus",
            unidade="Unig",
            oldExternalId="123456",
            newExternalId="654321"
        )

        created = self.entityService.create_entity(
            entityInput
        )

        created.entity_name = "teste"

        updated = self.entityService.update_entity(
            created
        )

        assert updated.entity_name == "teste"

    def test_delete_entity(self):

        entityInput = EntitysInput(
            sistema="Sophia",
            entity_name="campus",
            unidade="Unig",
            oldExternalId="123456",
            newExternalId="654321"
        )

        created = self.entityService.create_entity(
            entityInput
        )

        deleted = self.entityService.delete_entity(
            created.id
        )

        assert isinstance(deleted, EntitysModel)

        result = self.entityService.find_by_id_entity(
            created.id
        )

        assert result is None
        
        
