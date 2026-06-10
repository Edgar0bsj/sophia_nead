from datetime import date

import pytest

from src.dto.cat_disciplina_DTO import CategoriasDaDisciplinaInputDTO
from src.controllers.cat_disciplina_controller import CategoriasDaDisciplinaController


@pytest.fixture
def controller():
    controller = CategoriasDaDisciplinaController()
    return controller


class TestCategoriasDaDisciplinaController:

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_create_catDiscip(self, controller: CategoriasDaDisciplinaController):
        catDiscip_input = CategoriasDaDisciplinaInputDTO(
            sistema="SOPHIA",
            unidade="NOVA IGUAÇU",
            name="Estudos Dirigidos",
            externalId="directed_studies",
            subjectCategoryTypeId="directed_studies",
            isActive=True,
        )

        print(controller.create_cat_disciplina(catDiscip_input))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_find_all_carDiscip(self, controller: CategoriasDaDisciplinaController):
        all_catDiscipl = controller.find_all_catDiscip()

        print(all_catDiscipl)

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_update_catDiscip(self, controller: CategoriasDaDisciplinaController):
        ultimoRegistro = controller.find_all_catDiscip()
        ultimoRegistro = ultimoRegistro[-1]
        id = ultimoRegistro["id"]
        catDiscip_entity = CategoriasDaDisciplinaInputDTO(
            ultimoRegistro["sistema"],
            ultimoRegistro["unidade"],
            ultimoRegistro["name"],
            ultimoRegistro["externalId"],
            ultimoRegistro["subjectCategoryTypeId"],
            False,
        )

        print(controller.update_catDiscip(id, catDiscip_entity))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_delete_catDiscip(self, controller: CategoriasDaDisciplinaController):

        cat_discip = controller.find_all_catDiscip()[-1]

        controller.delete_cat_discip(cat_discip["id"])

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_export_catDiscip_CSV(self, controller: CategoriasDaDisciplinaController):
        controller.export_entity_to_CSV()
