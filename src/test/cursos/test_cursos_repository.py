import pytest

from src.models.cursos_model import CursosModel
from src.database.database_connection import DatabaseConnection
from src.repositories.cursos_repository import CursosRepository


@pytest.fixture
def repository():
    session = DatabaseConnection().bootstrap()
    repository = CursosRepository(session())
    return repository


@pytest.fixture
def cursos_model():
    return CursosModel(
        sistema="SOPHIA",
        unidade="UNIG",
        cursos_name="Extensão",
        externalId="123",
        isActive=True,
        externalTeachingModalityId="2154545",
        externalEducationLevelId="121545",
        courseTypeId="TEST-TYPEID",
    )


class TestCursosRepository:

    def test_create(
        self,
        repository: CursosRepository,
        cursos_model: CursosModel,
    ):

        resultCreate = repository.save(cursos_model)

        assert isinstance(resultCreate, CursosModel)
        assert resultCreate is not None

    def test_update(
        self,
        repository: CursosRepository,
        cursos_model: CursosModel,
    ):
        resultCreate = repository.save(cursos_model)

        resultCreate.sistema = "AVALIA"
        resultCreate.unidade = "UNIG"
        resultCreate.cursos_name = "EXTRA CURRICULAR"
        resultCreate.externalId = "321"
        resultCreate.isActive = True
        resultCreate.externalTeachingModalityId = "Pós-graduação"
        resultCreate.externalEducationLevelId = "Pós-graduação"
        resultCreate.courseTypeId = "Pós-graduação"

        resultUpdate = repository.update(resultCreate)

        assert isinstance(resultUpdate, CursosModel)
        assert resultCreate is not None
        assert resultUpdate.id == resultCreate.id
        assert resultUpdate.sistema == resultCreate.sistema
        assert resultUpdate.unidade == resultCreate.unidade
        assert resultUpdate.cursos_name == resultCreate.cursos_name
        assert resultUpdate.externalId == resultCreate.externalId
        assert resultUpdate.isActive == resultCreate.isActive
        assert (
            resultUpdate.externalTeachingModalityId
            == resultCreate.externalTeachingModalityId
        )
        assert (
            resultUpdate.externalEducationLevelId
            == resultCreate.externalEducationLevelId
        )
        assert resultUpdate.courseTypeId == resultCreate.courseTypeId

    def test_find_all(self, repository: CursosRepository):
        getAll = repository.find_all()

        assert getAll is not None
        assert isinstance(getAll, list)

        if len(getAll) > 0:
            for i in getAll:
                assert isinstance(i, CursosModel)

    def test_find_by_id(
        self,
        repository: CursosRepository,
        cursos_model: CursosModel,
    ):
        resultCreate = repository.save(cursos_model)

        findId = repository.find_by_id(resultCreate.id)

        assert findId is not None
        assert findId == resultCreate

    def test_delete(
        self,
        repository: CursosRepository,
        cursos_model: CursosModel,
    ):
        modaCreated = repository.save(cursos_model)

        resultDelete = repository.delete(modaCreated.id)

        deveSerNone = repository.find_by_id(resultDelete.id)

        assert deveSerNone is None
        assert resultDelete is not None
        assert resultDelete == modaCreated
