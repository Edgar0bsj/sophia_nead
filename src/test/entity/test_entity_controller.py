from datetime import date

import pytest

from src.dto.entityDTO import EntityInputDTO
from src.controllers.entity_controller import EntityController


@pytest.fixture
def controller():
    controller = EntityController()
    return controller


class TestEntityController:

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_create_entity(self, controller: EntityController):
        entity_input = EntityInputDTO(
            sistema="SOPHIA",
            unidade="NOVA IGUAÇU",
            entity_name="campus",
            oldExternalId="987654321",
            newExternalId="123456789",
        )

        print(controller.create_entity(entity_input))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_find_all_entity(self, controller: EntityController):
        all_entitys = controller.find_all_entity()

        print(all_entitys)

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_update_entity(self, controller: EntityController):
        ultimoRegistro = controller.find_all_entity()
        ultimoRegistro = ultimoRegistro[-1]
        id = ultimoRegistro["id"]
        edit_entity = EntityInputDTO(
            ultimoRegistro["sistema"],
            ultimoRegistro["unidade"],
            "campus",
            ultimoRegistro["oldExternalId"],
            ultimoRegistro["newExternalId"],
        )

        print(controller.update_entity(id, edit_entity))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_delete_entity(self, controller: EntityController):

        entity = controller.find_all_entity()[-1]

        controller.delete_entity(entity["id"])

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_export_entity_CSV(self, controller: EntityController):
        controller.export_entity_to_CSV()
