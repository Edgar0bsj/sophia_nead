import pytest

from src.database.database_connection import DatabaseConnection
from src.models.pessoas_model import PessoasModel
from src.repositories.pessoas_repository import PessoasRepository


@pytest.fixture
def repository():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = PessoasRepository(session())
    return repository


@pytest.fixture
def pessoas_model():
    return PessoasModel(
        sistema="SOPHIA",
        unidade="UNIG",
        pessoa_name="cateDisciplinaNome",
        socialName="cateDisciplinaNome",
        identityDocument="cateDisciplinaNome",
        identityDocumentTypeId="cateDisciplinaNome",
        passportNumber="cateDisciplinaNome",
        externalId="cateDisciplinaNome",
        address_zipCode="cateDisciplinaNome",
        address_state="cateDisciplinaNome",
        address_city="cateDisciplinaNome",
        address_address="cateDisciplinaNome",
        address_number="cateDisciplinaNome",
        address_neighborhood="cateDisciplinaNome",
        address_complement="cateDisciplinaNome",
        user_email="cateDisciplinaNome",
        user_username="cateDisciplinaNome",
        user_password="cateDisciplinaNome",
        tags="cateDisciplinaNome",
    )


class TestPessoasRepository:

    def test_create(
        self,
        repository: PessoasRepository,
        pessoas_model: PessoasModel,
    ):

        resultCreate = repository.save(pessoas_model)

        assert isinstance(resultCreate, PessoasModel)
        assert resultCreate is not None

    def test_update(
        self,
        repository: PessoasRepository,
        pessoas_model: PessoasModel,
    ):
        resultCreate = repository.save(pessoas_model)

        resultCreate.sistema = "AVALIA"
        resultCreate.unidade = "UNIG"
        resultCreate.pessoa_name = "ubirajara"

        resultUpdate = repository.update(resultCreate)

        assert isinstance(resultUpdate, PessoasModel)
        assert resultCreate is not None
        assert resultUpdate.id == resultCreate.id
        assert resultUpdate.sistema == resultCreate.sistema
        assert resultUpdate.pessoa_name == resultCreate.pessoa_name

    def test_find_all(self, repository: PessoasRepository):
        getAll = repository.find_all()

        assert getAll is not None
        assert isinstance(getAll, list)

        if len(getAll) > 0:
            for i in getAll:
                assert isinstance(i, PessoasModel)

    def test_find_by_id(
        self,
        repository: PessoasRepository,
        pessoas_model: PessoasModel,
    ):
        resultCreate = repository.save(pessoas_model)

        findId = repository.find_by_id(resultCreate.id)

        assert findId is not None
        assert findId == resultCreate

    def test_delete(
        self,
        repository: PessoasRepository,
        pessoas_model: PessoasModel,
    ):
        modaCreated = repository.save(pessoas_model)

        resultDelete = repository.delete(modaCreated.id)

        deveSerNone = repository.find_by_id(resultDelete.id)

        assert deveSerNone is None
        assert resultDelete is not None
        assert resultDelete == modaCreated
