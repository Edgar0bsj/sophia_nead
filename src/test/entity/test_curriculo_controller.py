from datetime import date

import pytest

from src.dto.curriculoDTO import CurriculoInputDTO
from src.controllers.curriculo_controller import CurriculoController


@pytest.fixture
def controller():
    controller = CurriculoController()
    return controller


class TestCurriculoController:

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_curriculo_entity(self, controller: CurriculoController):
        curriculo_input = CurriculoInputDTO(
            sistema="SOPHIA",
            unidade="NOVA IGUAÇU",
            externalCourseId="G_BIOMED",
            name="BIOMEDICINA",
            externalId="189",
            workload=1200,
            startDate=None,
            endDate=None,
            isActive=True,
        )

        print(controller.create_curriculo(curriculo_input))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_find_all_curriculo(self, controller: CurriculoController):
        all_curriculo = controller.find_all_curriculo()

        print(all_curriculo)

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_update_curriculo(self, controller: CurriculoController):
        ultimoRegistro = controller.find_all_curriculo()
        ultimoRegistro = ultimoRegistro[-1]
        id = ultimoRegistro["id"]
        edit_curriculo = CurriculoInputDTO(
            ultimoRegistro["sistema"],
            ultimoRegistro["unidade"],
            ultimoRegistro["externalCourseId"],
            ultimoRegistro["name"],
            ultimoRegistro["externalId"],
            ultimoRegistro["workload"],
            ultimoRegistro["startDate"],
            ultimoRegistro["endDate"],
            False,
        )

        print(controller.update_curriculo(id, edit_curriculo))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_delete_curriculo(self, controller: CurriculoController):

        curriculo = controller.find_all_curriculo()[-1]

        controller.delete_curriculo(curriculo["id"])

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_export_entity_CSV(self, controller: CurriculoController):
        controller.export_curriculo_to_CSV()
