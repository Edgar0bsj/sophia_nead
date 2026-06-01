import pytest

from src.models.nivelDeEnsino_model import NivelDeEnsinoModel
from src.database.database_connection import DatabaseConnection
from src.repositories.nivelDeEnsino_repository import NivelDeEnsinoRepository


@pytest.fixture
def repository():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = NivelDeEnsinoRepository(session())
    return repository


@pytest.fixture
def nivelDeEnsino_Model():
    return NivelDeEnsinoModel(
        sistema="SOPHIA",
        unidade="UNIG",
        NivelDeEnsino_name="Extensão",
        externalId="123",
        educationLevelTypeId="Graduação",
    )


class TestNivelDeEnsinoRepository:

    def test_create(
        self,
        repository: NivelDeEnsinoRepository,
        nivelDeEnsino_Model: NivelDeEnsinoModel,
    ):

        resultCreate = repository.save(nivelDeEnsino_Model)

        assert isinstance(resultCreate, NivelDeEnsinoModel)
        assert resultCreate is not None

    def test_update(
        self,
        repository: NivelDeEnsinoRepository,
        nivelDeEnsino_Model: NivelDeEnsinoModel,
    ):
        resultCreate = repository.save(nivelDeEnsino_Model)

        resultCreate.sistema = "AVALIA"
        resultCreate.unidade = "UNIG"
        resultCreate.NivelDeEnsino_name = "EXTRA CURRICULAR"
        resultCreate.externalId = "321"
        resultCreate.educationLevelTypeId = "Pós-graduação"

        resultUpdate = repository.update(resultCreate)

        assert isinstance(resultUpdate, NivelDeEnsinoModel)
        assert resultCreate is not None
        assert resultUpdate.id == resultCreate.id
        assert resultUpdate.sistema == resultCreate.sistema
        assert resultUpdate.unidade == resultCreate.unidade
        assert resultUpdate.NivelDeEnsino_name == resultCreate.NivelDeEnsino_name
        assert resultUpdate.externalId == resultCreate.externalId
        assert resultUpdate.educationLevelTypeId == resultCreate.educationLevelTypeId

    def test_find_all(self, repository: NivelDeEnsinoRepository):
        nivelDeEnsinoAll = repository.find_all()

        assert nivelDeEnsinoAll is not None
        assert isinstance(nivelDeEnsinoAll, list)

        if len(nivelDeEnsinoAll) > 0:
            for i in nivelDeEnsinoAll:
                assert isinstance(i, NivelDeEnsinoModel)

    def test_find_by_id(
        self,
        repository: NivelDeEnsinoRepository,
        nivelDeEnsino_Model: NivelDeEnsinoRepository,
    ):
        resultCreate = repository.save(nivelDeEnsino_Model)

        findId = repository.find_by_id(resultCreate.id)

        assert findId is not None
        assert findId == resultCreate

    def test_delete(
        self,
        repository: NivelDeEnsinoRepository,
        nivelDeEnsino_Model: NivelDeEnsinoModel,
    ):
        modaCreated = repository.save(nivelDeEnsino_Model)

        resultDelete = repository.delete(modaCreated.id)

        deveSerNone = repository.find_by_id(resultDelete.id)

        assert deveSerNone is None
        assert resultDelete is not None
        assert resultDelete == modaCreated
