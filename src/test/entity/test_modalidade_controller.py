import pytest

from src.dto.modalidadeDTO import ModalidadeInputDTO
from src.controllers.modalidade_controller import ModalidadeController


@pytest.fixture
def controller():
    controller = ModalidadeController()
    return controller


class TestModalidadeController:

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_create_modalidade(self, controller: ModalidadeController):
        modalidade_input = ModalidadeInputDTO(
            sistema="SOPHIA",
            unidade="NOVA IGUAÇU",
            modalidade_nome="Semipresencial",
            externalId="6",
            teachingModalityTypeId="blended_learning",
        )

        print(controller.create_modalidade(modalidade_input))

    # @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_find_all_modalidade(self, controller: ModalidadeController):
        all_modalidade = controller.find_all_modalidade()

        print(all_modalidade)

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_update_modalidade(self, controller: ModalidadeController):
        ultimoRegistro = controller.find_all_modalidade()
        ultimoRegistro = ultimoRegistro[-1]
        edit_modali = ModalidadeInputDTO(
            ultimoRegistro["sistema"],
            ultimoRegistro["unidade"],
            ultimoRegistro["modalidade_nome"],
            ultimoRegistro["externalId"],
            teachingModalityTypeId="distance_learning",
        )
        id = ultimoRegistro["id"]

        print(controller.update_modalidade(id, edit_modali))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_delete_entity(self, controller: ModalidadeController):

        modalidade = controller.find_all_modalidade()[-1]

        controller.delete_modalidade(modalidade["id"])

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_export_entity_CSV(self, controller: ModalidadeController):
        controller.export_modalidade_to_CSV()

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_get_cursos_by_modalidade(self, controller: ModalidadeController):
        controller.get_cursos_by_modalidade(1)
