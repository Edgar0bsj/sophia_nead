from src.containers.entity_container import entityContainer
from src.dto.entityDTO import EntityDTO
from src.models.entitys_model import EntitysModel
from typing import List

class TestEntityService:

    def setup_method(self):
        self.controller = entityContainer()

    def test_create_entity(self):

        entity_campus = EntityDTO(
            sistema="SOPHIA",
            unidade="UNIG",
            entity_name="campus",
            oldExternalId="741852963",
            newExternalId="369258147"
        )

        result = self.controller.create_entity(entity_campus)

        assert isinstance(result, EntitysModel)

        assert result.id is not None

        assert result.entity_name == "campus"

    def test_find_all_entity(self):
        
        entity_all = self.controller.find_all_entity()
        
        assert isinstance(entity_all, list)

        for idx in range(len(entity_all)):
            assert isinstance(entity_all[idx], EntitysModel)
            
    def test_find_by_id_entity(self):
        
        entity_campus = EntityDTO(
            sistema="SOPHIA",
            unidade="UNIG",
            entity_name="campus",
            oldExternalId="741852963",
            newExternalId="369258147"
        )
        
        created = self.controller.create_entity(entity_campus)
        
        result = self.controller.find_by_id_entity(created.id)
        
        assert isinstance(result, EntitysModel)
        assert created.id == result.id