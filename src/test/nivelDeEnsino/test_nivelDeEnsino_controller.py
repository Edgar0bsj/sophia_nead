import pytest

from src.models.nivelDeEnsino_model import NivelDeEnsinoModel
from src.database.database_connection import DatabaseConnection

from src.services.nivelDeEnsino_service import NivelDeEnsinoService
from src.repositories.nivelDeEnsino_repository import NivelDeEnsinoRepository

from src.controllers.nivelDeEnsino_controller import NivelDeEnsinoController


@pytest.fixture
def controller():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = NivelDeEnsinoRepository(session())

    service = NivelDeEnsinoService(repository)
    controller = NivelDeEnsinoController(service)
    return controller


@pytest.fixture
def nivelDeEnsino_Model():
    return NivelDeEnsinoModel(
        sistema="SOPHIA",
        unidade="UNIG",
        NivelDeEnsino_name="Extensão",
        externalId="123",
        educationLevelTypeId="Graduação",
    )


class TestNivelDeEnsinoController:

    def test_create_nivelDeEnsino(
        self,
        controller: NivelDeEnsinoController,
        nivelDeEnsino_Model: NivelDeEnsinoModel,
    ):
        created = controller.create_nivelDeEnsino(nivelDeEnsino_Model)

        assert created is not None
        assert isinstance(created, NivelDeEnsinoModel)

    def test_update_nivelDeEnsino(
        self,
        controller: NivelDeEnsinoController,
        nivelDeEnsino_Model: NivelDeEnsinoModel,
    ):
        created = controller.create_nivelDeEnsino(nivelDeEnsino_Model)

        created.entity_name = "buzios"

        result = controller.update_nivelDeEnsino(created)

        assert result is not None
        assert isinstance(result, NivelDeEnsinoModel)
        assert result.id == created.id
        assert result.entity_name == created.entity_name

    def test_find_all_nivelDeEnsino(self, controller: NivelDeEnsinoController):
        result = controller.find_all_nivelDeEnsino()

        assert result is not None
        assert isinstance(result, list)
        for i in result:
            assert isinstance(i, NivelDeEnsinoModel)

    def test_find_by_id_nivelDeEnsino(
        self,
        controller: NivelDeEnsinoController,
        nivelDeEnsino_Model: NivelDeEnsinoModel,
    ):

        created = controller.create_nivelDeEnsino(nivelDeEnsino_Model)

        resultFind = controller.find_by_id_nivelDeEnsino(created.id)

        assert resultFind.id == created.id
        assert isinstance(resultFind, NivelDeEnsinoModel)
        assert resultFind is not None

    def test_remove_nivelDeEnsino(
        self,
        controller: NivelDeEnsinoController,
        nivelDeEnsino_Model: NivelDeEnsinoModel,
    ):
        created = controller.create_nivelDeEnsino(nivelDeEnsino_Model)

        removeResult = controller.remove_nivelDeEnsino(created.id)

        assert removeResult is not None
        assert isinstance(removeResult, NivelDeEnsinoModel)
        assert removeResult.id == created.id
