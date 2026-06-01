import pytest

from src.models.modalidade_model import ModalidadeModel
from src.database.database_connection import DatabaseConnection

from src.services.modalidade_service import ModalidadeService
from src.repositories.modalidade_repository import ModalidadeRepository


@pytest.fixture
def service():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = ModalidadeRepository(session())

    service = ModalidadeService(repository)
    return service


@pytest.fixture
def entity_model():
    return ModalidadeModel(
        sistema="SOPHIA",
        unidade="UNIG",
        modalidade_nome="Extensão",
        externalId="9",
        teachingModalityTypeId="blended_learning",
    )


class TestModalidadeService:

    def test_save(self, service: ModalidadeService, entity_model: ModalidadeModel):
        result = service.save(entity_model)

        assert result.externalId == entity_model.externalId
        assert result is not None
        assert isinstance(result, ModalidadeModel)

    def test_update(self, service: ModalidadeService, entity_model: ModalidadeModel):
        entityCreated = service.save(entity_model)

        entityCreated.sistema = "AVALIA"
        entityCreated.unidade = "ITAPERUNA"
        entityCreated.modalidade_nome = "polo"
        entityCreated.externalId = "1112223344"
        entityCreated.teachingModalityTypeId = "6655443322"

        result = service.update(entityCreated)

        assert result.id == entityCreated.id
        assert result is not None
        assert isinstance(result, ModalidadeModel)

    def test_find_by_id(
        self, service: ModalidadeService, entity_model: ModalidadeModel
    ):
        created = service.save(entity_model)

        findResult = service.find_by_id(created.id)

        assert findResult is not None
        assert isinstance(findResult, ModalidadeModel)
        assert findResult.id == created.id

    def test_find_all(self, service: ModalidadeService):
        result = service.find_all()

        assert result is not None
        assert isinstance(result, list)
        if len(result) > 0:
            for i in result:
                assert isinstance(i, ModalidadeModel)

    def test_delete(self, service: ModalidadeService, entity_model: ModalidadeModel):
        created = service.save(entity_model)

        result = service.delete(created.id)

        deveSerNone = service.find_by_id(created.id)

        assert result is not None
        assert isinstance(result, ModalidadeModel)
        assert deveSerNone is None

    # def test_update_insert_entity(self, service: ModalidadeService):
    #     entity_1 = ModalidadeModel(
    #         sistema="TESTE",
    #         unidade="TESTEE",
    #         entity_name="campusS",
    #         oldExternalId="123456789",
    #         newExternalId="987654321",
    #     )

    #     created_entity_1 = service.save(entity_1)

    #     entity_2 = ModalidadeModel(
    #         sistema="TESTE",
    #         unidade="TESTEE",
    #         entity_name="campusS",
    #         oldExternalId="999999999",
    #         newExternalId="888888888",
    #     )

    #     created_entity_2 = service.save(entity_2)

    #     entity_1_output = service.find_by_id(created_entity_1.id)
    #     entity_2_output = service.find_by_id(created_entity_2.id)

    #     assert isinstance(entity_1_output, ModalidadeModel)
    #     assert isinstance(entity_2_output, ModalidadeModel)
    #     assert entity_1_output.id == entity_2_output.id
