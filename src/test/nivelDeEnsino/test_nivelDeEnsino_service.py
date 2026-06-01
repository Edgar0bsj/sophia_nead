import pytest

from src.models.nivelDeEnsino_model import NivelDeEnsinoModel
from src.database.database_connection import DatabaseConnection

from src.repositories.nivelDeEnsino_repository import NivelDeEnsinoRepository
from src.services.nivelDeEnsino_service import NivelDeEnsinoService


@pytest.fixture
def service():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = NivelDeEnsinoRepository(session())

    service = NivelDeEnsinoService(repository)
    return service


@pytest.fixture
def nivelDeEnsino_Model():
    return NivelDeEnsinoModel(
        sistema="SOPHIA",
        unidade="UNIG",
        NivelDeEnsino_name="Extensão",
        externalId="123",
        educationLevelTypeId="Graduação",
    )


class TestNivelDeEnsinoService:

    def test_save(
        self, service: NivelDeEnsinoService, nivelDeEnsino_Model: NivelDeEnsinoModel
    ):
        result = service.save(nivelDeEnsino_Model)

        assert result.externalId == nivelDeEnsino_Model.externalId
        assert result is not None
        assert isinstance(result, NivelDeEnsinoModel)

    def test_update(
        self, service: NivelDeEnsinoService, nivelDeEnsino_Model: NivelDeEnsinoModel
    ):
        entityCreated = service.save(nivelDeEnsino_Model)

        entityCreated.sistema = "AVALIA"
        entityCreated.unidade = "ITAPERUNA"
        entityCreated.NivelDeEnsino_name = "polo"
        entityCreated.externalId = "1112223344"
        entityCreated.educationLevelTypeId = "6655443322"

        result = service.update(entityCreated)

        assert result.id == entityCreated.id
        assert result.sistema == entityCreated.sistema
        assert result.unidade == entityCreated.unidade
        assert result.NivelDeEnsino_name == entityCreated.NivelDeEnsino_name
        assert result.externalId == entityCreated.externalId
        assert result.educationLevelTypeId == entityCreated.educationLevelTypeId
        assert result is not None
        assert isinstance(result, NivelDeEnsinoModel)

    def test_find_by_id(
        self, service: NivelDeEnsinoService, nivelDeEnsino_Model: NivelDeEnsinoModel
    ):
        created = service.save(nivelDeEnsino_Model)

        findResult = service.find_by_id(created.id)

        assert findResult is not None
        assert isinstance(findResult, NivelDeEnsinoModel)
        assert findResult.id == created.id

    def test_find_all(self, service: NivelDeEnsinoService):
        result = service.find_all()

        assert result is not None
        assert isinstance(result, list)
        if len(result) > 0:
            for i in result:
                assert isinstance(i, NivelDeEnsinoModel)

    def test_delete(
        self, service: NivelDeEnsinoService, nivelDeEnsino_Model: NivelDeEnsinoModel
    ):
        created = service.save(nivelDeEnsino_Model)

        result = service.delete(created.id)

        deveSerNone = service.find_by_id(created.id)

        assert result is not None
        assert isinstance(result, NivelDeEnsinoModel)
        assert deveSerNone is None
