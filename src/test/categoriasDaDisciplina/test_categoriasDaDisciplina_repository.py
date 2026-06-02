import pytest

from src.database.database_connection import DatabaseConnection
from src.models.categoriasDaDisciplina_model import CategoriasDaDiciplinaModel
from src.repositories.categoriasDaDisciplina_repository import (
    CategoriasDaDisciplinaRepository,
)


@pytest.fixture
def repository():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = CategoriasDaDisciplinaRepository(session())
    return repository


@pytest.fixture
def categoriasDaDiciplina_model():
    return CategoriasDaDiciplinaModel(
        sistema="SOPHIA",
        unidade="UNIG",
        categoria_da_diciplina_name="cateDisciplinaNome",
        externalId="externalIDDIDID",
        subjectCategoryTypeId="idtype262626",
        isActive=True,
    )


class TestCategoriasDaDiciplinaRepository:

    def test_create(
        self,
        repository: CategoriasDaDisciplinaRepository,
        categoriasDaDiciplina_model: CategoriasDaDiciplinaModel,
    ):

        resultCreate = repository.save(categoriasDaDiciplina_model)

        assert isinstance(resultCreate, CategoriasDaDiciplinaModel)
        assert resultCreate is not None

    def test_update(
        self,
        repository: CategoriasDaDisciplinaRepository,
        categoriasDaDiciplina_model: CategoriasDaDiciplinaModel,
    ):
        resultCreate = repository.save(categoriasDaDiciplina_model)

        resultCreate.sistema = "AVALIA"
        resultCreate.unidade = "UNIG"
        resultCreate.categoria_da_diciplina_name = "polusdelux"
        resultCreate.externalId = "cascadura"
        resultCreate.subjectCategoryTypeId = "TesteTest"
        resultCreate.isActive = False

        resultUpdate = repository.update(resultCreate)

        assert isinstance(resultUpdate, CategoriasDaDiciplinaModel)
        assert resultCreate is not None
        assert resultUpdate.id == resultCreate.id
        assert resultUpdate.sistema == resultCreate.sistema
        assert resultUpdate.unidade == resultCreate.unidade
        assert (
            resultUpdate.categoria_da_diciplina_name
            == resultCreate.categoria_da_diciplina_name
        )
        assert resultUpdate.externalId == resultCreate.externalId
        assert resultUpdate.subjectCategoryTypeId == resultCreate.subjectCategoryTypeId
        assert resultUpdate.isActive == resultCreate.isActive

    def test_find_all(self, repository: CategoriasDaDisciplinaRepository):
        getAll = repository.find_all()

        assert getAll is not None
        assert isinstance(getAll, list)

        if len(getAll) > 0:
            for i in getAll:
                assert isinstance(i, CategoriasDaDiciplinaModel)

    def test_find_by_id(
        self,
        repository: CategoriasDaDisciplinaRepository,
        categoriasDaDiciplina_model: CategoriasDaDiciplinaModel,
    ):
        resultCreate = repository.save(categoriasDaDiciplina_model)

        findId = repository.find_by_id(resultCreate.id)

        assert findId is not None
        assert findId == resultCreate

    def test_delete(
        self,
        repository: CategoriasDaDisciplinaRepository,
        categoriasDaDiciplina_model: CategoriasDaDiciplinaModel,
    ):
        modaCreated = repository.save(categoriasDaDiciplina_model)

        resultDelete = repository.delete(modaCreated.id)

        deveSerNone = repository.find_by_id(resultDelete.id)

        assert deveSerNone is None
        assert resultDelete is not None
        assert resultDelete == modaCreated
