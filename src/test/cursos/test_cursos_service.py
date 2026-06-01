import pytest

from src.models.cursos_model import CursosModel
from src.database.database_connection import DatabaseConnection

from src.repositories.cursos_repository import CursosRepository
from src.services.cursos_service import CursosServices


@pytest.fixture
def service():
    session = DatabaseConnection().bootstrap()
    repository = CursosRepository(session())

    service = CursosServices(repository)
    return service


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


class TestCursosService:

    def test_save(self, service: CursosServices, cursos_model: CursosModel):
        result = service.save(cursos_model)

        assert result.externalId == cursos_model.externalId
        assert result is not None
        assert isinstance(result, CursosModel)

    def test_update(self, service: CursosServices, cursos_model: CursosModel):
        cursosCreated = service.save(cursos_model)

        cursosCreated.sistema = "AVALIA"
        cursosCreated.unidade = "ITAPERUNA"
        cursosCreated.cursos_name = "polo"
        cursosCreated.externalId = "1112223344"
        cursosCreated.isActive = True
        cursosCreated.externalTeachingModalityId = "alalala"
        cursosCreated.externalEducationLevelId = "alalala"
        cursosCreated.courseTypeId = "alalala"

        result = service.update(cursosCreated)

        assert result.id == cursosCreated.id
        assert result.sistema == cursosCreated.sistema
        assert result.unidade == cursosCreated.unidade
        assert result.cursos_name == cursosCreated.cursos_name
        assert result.externalId == cursosCreated.externalId
        assert result.isActive == cursosCreated.isActive
        assert (
            result.externalTeachingModalityId
            == cursosCreated.externalTeachingModalityId
        )
        assert result.externalEducationLevelId == cursosCreated.externalEducationLevelId
        assert result.courseTypeId == cursosCreated.courseTypeId
        assert result is not None
        assert isinstance(result, CursosModel)

    def test_find_by_id(self, service: CursosServices, cursos_model: CursosModel):
        created = service.save(cursos_model)

        findResult = service.find_by_id(created.id)

        assert findResult is not None
        assert isinstance(findResult, CursosModel)
        assert findResult.id == created.id

    def test_find_all(self, service: CursosServices):
        result = service.find_all()

        assert result is not None
        assert isinstance(result, list)
        if len(result) > 0:
            for i in result:
                assert isinstance(i, CursosModel)

    def test_delete(self, service: CursosServices, cursos_model: CursosModel):
        created = service.save(cursos_model)

        result = service.delete(created.id)

        deveSerNone = service.find_by_id(created.id)

        assert result is not None
        assert isinstance(result, CursosModel)
        assert deveSerNone is None
