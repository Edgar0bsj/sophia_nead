import pytest

from src.models.modalidade_model import ModalidadeModel
from src.database.database_connection import DatabaseConnection
from src.repositories.modalidade_repository import ModalidadeRepository


@pytest.fixture
def repository():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = ModalidadeRepository(session())
    return repository


@pytest.fixture
def modalidade_Model():
    return ModalidadeModel(
        sistema="SOPHIA",
        unidade="UNIG",
        modalidade_nome="Extensão",
        externalId="9",
        teachingModalityTypeId="blended_learning",
    )


class TestModalidadeRepository:

    def test_create(
        self, repository: ModalidadeRepository, modalidade_Model: ModalidadeModel
    ):

        resultCreate = repository.save(modalidade_Model)

        assert isinstance(resultCreate, ModalidadeModel)
        assert resultCreate is not None

    def test_update(
        self, repository: ModalidadeRepository, modalidade_Model: ModalidadeModel
    ):
        resultCreate = repository.save(modalidade_Model)

        resultCreate.sistema = "AVALIA"
        resultCreate.unidade = "UNIG"
        resultCreate.modalidade_nome = "EXTRA CURRICULAR"
        resultCreate.externalId = "10"
        resultCreate.teachingModalityTypeId = "TESTE"

        resultUpdate = repository.update(resultCreate)

        assert isinstance(resultUpdate, ModalidadeModel)
        assert resultCreate is not None
        assert resultUpdate.id == resultCreate.id
        assert resultUpdate.sistema == resultCreate.sistema
        assert resultUpdate.unidade == resultCreate.unidade
        assert resultUpdate.modalidade_nome == resultCreate.modalidade_nome
        assert resultUpdate.externalId == resultCreate.externalId
        assert (
            resultUpdate.teachingModalityTypeId == resultCreate.teachingModalityTypeId
        )

    def test_find_all(self, repository: ModalidadeRepository):
        modalidadeAll = repository.find_all()

        assert modalidadeAll is not None
        assert isinstance(modalidadeAll, list)
        for i in modalidadeAll:
            assert isinstance(i, ModalidadeModel)

    def test_find_by_id(
        self, repository: ModalidadeRepository, modalidade_Model: ModalidadeModel
    ):
        resultCreate = repository.save(modalidade_Model)

        findId = repository.find_by_id(resultCreate.id)

        assert findId is not None
        assert findId == resultCreate

    def test_delete(
        self, repository: ModalidadeRepository, modalidade_Model: ModalidadeModel
    ):
        modaCreated = repository.save(modalidade_Model)

        resultDelete = repository.delete(modaCreated.id)

        deveSerNone = repository.find_by_id(resultDelete.id)

        assert deveSerNone is None
        assert resultDelete is not None
        assert resultDelete == modaCreated
