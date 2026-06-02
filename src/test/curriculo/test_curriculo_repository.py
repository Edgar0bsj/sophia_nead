from datetime import date

import pytest

from src.models.curriculo_model import CurriculoModel
from src.database.database_connection import DatabaseConnection
from src.repositories.curriculo_repository import CurriculoRepository


@pytest.fixture
def repository():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = CurriculoRepository(session())
    return repository


@pytest.fixture
def curriculo_model():
    return CurriculoModel(
        sistema="SOPHIA",
        unidade="UNIG",
        externalCourseId="campusPolo",
        curriculo_name="nomesDeTesteDoCurriculo",
        externalId="123151542121",
        workload=32165498,
        startDate=date(2026, 6, 2),
        endDate=date(2026, 7, 15),
        isActive=True,
    )


class TestCurriculoRepository:

    def test_create(
        self,
        repository: CurriculoRepository,
        curriculo_model: CurriculoModel,
    ):

        resultCreate = repository.save(curriculo_model)

        assert isinstance(resultCreate, CurriculoModel)
        assert resultCreate is not None

    def test_update(
        self,
        repository: CurriculoRepository,
        curriculo_model: CurriculoModel,
    ):
        resultCreate = repository.save(curriculo_model)

        resultCreate.sistema = "AVALIA"
        resultCreate.unidade = "UNIG"
        resultCreate.externalCourseId = "polusdelux"
        resultCreate.curriculo_name = "cascadura"
        resultCreate.externalId = "TesteTest"
        resultCreate.workload = 963852741
        resultCreate.startDate = date(2026, 8, 26)
        resultCreate.endDate = date(2026, 6, 20)
        resultCreate.isActive = False

        resultUpdate = repository.update(resultCreate)

        assert isinstance(resultUpdate, CurriculoModel)
        assert resultCreate is not None
        assert resultUpdate.id == resultCreate.id
        assert resultUpdate.sistema == resultCreate.sistema
        assert resultUpdate.unidade == resultCreate.unidade
        assert resultUpdate.externalCourseId == resultCreate.externalCourseId
        assert resultUpdate.curriculo_name == resultCreate.curriculo_name
        assert resultUpdate.externalId == resultCreate.externalId
        assert resultUpdate.workload == resultCreate.workload
        assert resultUpdate.startDate == resultCreate.startDate
        assert resultUpdate.endDate == resultCreate.endDate
        assert resultUpdate.isActive == resultCreate.isActive

    def test_find_all(self, repository: CurriculoRepository):
        getAll = repository.find_all()

        assert getAll is not None
        assert isinstance(getAll, list)

        if len(getAll) > 0:
            for i in getAll:
                assert isinstance(i, CurriculoModel)

    def test_find_by_id(
        self,
        repository: CurriculoRepository,
        curriculo_model: CurriculoModel,
    ):
        resultCreate = repository.save(curriculo_model)

        findId = repository.find_by_id(resultCreate.id)

        assert findId is not None
        assert findId == resultCreate

    def test_delete(
        self,
        repository: CurriculoRepository,
        curriculo_model: CurriculoModel,
    ):
        modaCreated = repository.save(curriculo_model)

        resultDelete = repository.delete(modaCreated.id)

        deveSerNone = repository.find_by_id(resultDelete.id)

        assert deveSerNone is None
        assert resultDelete is not None
        assert resultDelete == modaCreated
