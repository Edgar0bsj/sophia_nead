import pytest

from src.models.modalidade_model import ModalidadeModel
from src.database.database_connection import DatabaseConnection

from src.services.modalidade_service import ModalidadeService
from src.repositories.modalidade_repository import ModalidadeRepository

from src.controllers.modalidade_controller import ModalidadeController


@pytest.fixture
def controller():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = ModalidadeRepository(session())

    service = ModalidadeService(repository)
    controller = ModalidadeController(service)
    return controller


@pytest.fixture
def modalidade_Model():
    return ModalidadeModel(
        sistema="SOPHIA",
        unidade="UNIG",
        modalidade_nome="Extensão",
        externalId="9",
        teachingModalityTypeId="blended_learning",
    )


class TestModalidadeController:

    def test_create_modalidade(
        self, controller: ModalidadeController, modalidade_Model: ModalidadeModel
    ):
        created = controller.create_modalidade(modalidade_Model)

        assert created is not None
        assert isinstance(created, ModalidadeModel)

    def test_update_modalidade(
        self, controller: ModalidadeController, modalidade_Model: ModalidadeModel
    ):
        created = controller.create_modalidade(modalidade_Model)

        created.entity_name = "buzios"

        result = controller.update_modalidade(created)

        assert result is not None
        assert isinstance(result, ModalidadeModel)
        assert result.id == created.id
        assert result.entity_name == created.entity_name

    def test_find_all_modalidade(self, controller: ModalidadeController):
        result = controller.find_all_modalidade()

        assert result is not None
        assert isinstance(result, list)
        for i in result:
            assert isinstance(i, ModalidadeModel)

    def test_find_by_id_modalidade(
        self, controller: ModalidadeController, modalidade_Model: ModalidadeModel
    ):

        created = controller.create_modalidade(modalidade_Model)

        resultFind = controller.find_by_id_modalidade(created.id)

        assert resultFind.id == created.id
        assert isinstance(resultFind, ModalidadeModel)
        assert resultFind is not None

    def test_remove_modalidade(
        self, controller: ModalidadeController, modalidade_Model: ModalidadeModel
    ):
        created = controller.create_modalidade(modalidade_Model)

        removeResult = controller.remove_modalidade(created.id)

        assert removeResult is not None
        assert isinstance(removeResult, ModalidadeModel)
        assert removeResult.id == created.id
