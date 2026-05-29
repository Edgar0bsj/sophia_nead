from src.containers.entity_container import entityContainer
from src.dto.entityDTO import EntityDTO
from src.models.entitys_model import EntitysModel

class TestEntityService:

    def setup_method(self):
        self.controller = entityContainer()
        self.entitysTeste = []
    
    def teardown_method(self):
        if len(self.entitysTeste) > 0:
            for i in range(len(self.entitysTeste)):
                self.controller.remove_entity(self.entitysTeste[i].id)

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
        self.entitysTeste.append(result)
        
        

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
        assert created.sistema == result.sistema
        assert created.unidade == result.unidade
        assert created.entity_name == result.entity_name
        assert created.oldExternalId == result.oldExternalId
        assert created.newExternalId == result.newExternalId
        self.entitysTeste.append(created)
        
    def test_update_entity(self):
        
        entity_campus = EntityDTO(
            sistema="SOPHIA",
            unidade="UNIG",
            entity_name="campus",
            oldExternalId="741852963",
            newExternalId="369258147"
        )
        
        created = self.controller.create_entity(entity_campus)
        
        created.sistema = "LXP"
        created.unidade = "ITAPERUNAT"
        created.entity_name = "polo"
        created.oldExternalId = "852147963"
        created.newExternalId = "963852741"
        
        update = self.controller.update_entity(created)
        
        result = self.controller.find_by_id_entity(created.id)
        
        assert isinstance(result, EntitysModel)
        assert update.id == created.id
        assert update.sistema == created.sistema
        assert update.unidade == created.unidade
        assert update.entity_name == created.entity_name
        assert update.oldExternalId == created.oldExternalId
        assert update.newExternalId == created.newExternalId
        self.entitysTeste.append(created)
        
    def test_delete_entity(self):
        entity_campus = EntityDTO(
            sistema="TESTE",
            unidade="UNIG",
            entity_name="campus",
            oldExternalId="741852963",
            newExternalId="369258147"
        )
        
        created = self.controller.create_entity(entity_campus)
        
        entity_dell = self.controller.remove_entity(created.id)

        assert isinstance(entity_dell, EntitysModel)
        assert len(self.entitysTeste) == 0
        self.entitysTeste.append(created)
        
    def test_update_insert_entity(self):
        entity_1 = EntityDTO(
            sistema="TESTE",
            unidade="TESTEE",
            entity_name="campusS",
            oldExternalId="123456789",
            newExternalId="987654321"
        )
        
        created_entity_1 =self.controller.create_entity(entity_1)
        
        entity_2 = EntityDTO(
            sistema="TESTE",
            unidade="TESTEE",
            entity_name="campusS",
            oldExternalId="999999999",
            newExternalId="888888888"
        )
        
        created_entity_2 = self.controller.create_entity(entity_2)

        entity_1_output = self.controller.find_by_id_entity(created_entity_1.id)
        entity_2_output = self.controller.find_by_id_entity(created_entity_2.id)
        
        assert isinstance(entity_1_output, EntitysModel)
        assert isinstance(entity_2_output, EntitysModel)
        assert entity_1_output.id == entity_2_output.id
        

            