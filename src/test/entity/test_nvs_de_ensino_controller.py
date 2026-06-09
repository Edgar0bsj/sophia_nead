from datetime import date

import pytest

from src.dto.niveis_de_ensinoDTO import NiveisDeEnsinoInputDTO
from src.controllers.niveis_de_ensino_controller import NiveisDeEnsinoController


@pytest.fixture
def controller():
    controller = NiveisDeEnsinoController()
    return controller


class TestNvsDeEnsinoController:

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_create_nvs_de_ensino(self, controller: NiveisDeEnsinoController):
        nvs_de_ensino_input = NiveisDeEnsinoInputDTO(
            sistema="SOPHIA",
            unidade="NOVA IGUAÇU",
            name="graduate",
            externalId="1",
            educationLevelTypeId="undergraduate",
        )

        print(controller.create_nvs_de_ensino(nvs_de_ensino_input))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_find_all_nvs_de_ensino(self, controller: NiveisDeEnsinoController):
        all_nvs_de_ensino = controller.find_all_nvs_de_ensino()

        print(all_nvs_de_ensino)

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_update_nvs_de_ensino(self, controller: NiveisDeEnsinoController):
        ultimoRegistro = controller.find_all_nvs_de_ensino()
        ultimoRegistro = ultimoRegistro[-1]
        id = ultimoRegistro["id"]
        edit_nvs_de_ensino = NiveisDeEnsinoInputDTO(
            ultimoRegistro["sistema"],
            ultimoRegistro["unidade"],
            ultimoRegistro["name"],
            ultimoRegistro["externalId"],
            "high_school",
        )

        print(controller.update_nvs_de_ensino(id, edit_nvs_de_ensino))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_delete_nvs_de_ensino(self, controller: NiveisDeEnsinoController):

        nvs_de_ensino = controller.find_all_nvs_de_ensino()[-1]

        controller.delete_nvs_de_ensino(nvs_de_ensino["id"])

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_export_nvs_de_ensino_CSV(self, controller: NiveisDeEnsinoController):
        controller.export_nvs_de_ensino_to_CSV()
