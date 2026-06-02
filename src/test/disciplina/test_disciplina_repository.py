import pytest

from src.database.database_connection import DatabaseConnection
from src.models.disciplinas_model import DisciplinasModel
from src.repositories.disciplina_repository import DisciplinaRepository


@pytest.fixture
def repository():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = DisciplinaRepository(session())
    return repository


@pytest.fixture
def disciplina_model():
    return DisciplinasModel(
        sistema="SOPHIA",
        unidade="UNIG",
        disciplina_name="nome da disciplina",
        externalId="striiiiinggg",
        workload=0,
        isActive=True,
        externalSubjectCategoryId="UNIG",
    )


class TestDisciplinaRepository:

    def test_create(
        self,
        repository: DisciplinaRepository,
        disciplina_model: DisciplinasModel,
    ):

        resultCreate = repository.save(disciplina_model)

        assert isinstance(resultCreate, DisciplinasModel)
        assert resultCreate is not None

    def test_update(
        self,
        repository: DisciplinaRepository,
        disciplina_model: DisciplinasModel,
    ):
        resultCreate = repository.save(disciplina_model)

        resultCreate.sistema = "AVALIA"
        resultCreate.unidade = "UNIG"
        resultCreate.externalId = "UMidLegal"

        resultUpdate = repository.update(resultCreate)

        assert isinstance(resultUpdate, DisciplinasModel)
        assert resultCreate is not None
        assert resultUpdate.id == resultCreate.id
        assert resultUpdate.sistema == resultCreate.sistema
        assert resultUpdate.externalId == resultCreate.externalId

    def test_find_all(self, repository: DisciplinaRepository):
        getAll = repository.find_all()

        assert getAll is not None
        assert isinstance(getAll, list)

        if len(getAll) > 0:
            for i in getAll:
                assert isinstance(i, DisciplinasModel)

    def test_find_by_id(
        self,
        repository: DisciplinaRepository,
        disciplina_model: DisciplinasModel,
    ):
        resultCreate = repository.save(disciplina_model)

        findId = repository.find_by_id(resultCreate.id)

        assert findId is not None
        assert findId == resultCreate

    def test_delete(
        self,
        repository: DisciplinaRepository,
        disciplina_model: DisciplinasModel,
    ):
        modaCreated = repository.save(disciplina_model)

        resultDelete = repository.delete(modaCreated.id)

        deveSerNone = repository.find_by_id(resultDelete.id)

        assert deveSerNone is None
        assert resultDelete is not None
        assert resultDelete == modaCreated
