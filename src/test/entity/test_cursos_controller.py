import pytest

from src.dto.cursosDTO import CursosInputDTO
from src.controllers.cursos_controller import CursosController


@pytest.fixture
def controller():
    controller = CursosController()
    return controller


class TestCursosController:

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_create_curso(self, controller: CursosController):
        curso_input = CursosInputDTO(
            sistema="SOPHIA",
            unidade="NOVA IGUAÇU",
            name="Biomedicina",
            externalId="G_BIOMED",
            isActive=True,
            externalTeachingModalityId="6",
            externalEducationLevelId="1",
            courseTypeId="bachelor",
        )

        print(controller.create_curso(curso_input))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_find_all_cursos(self, controller: CursosController):
        all_curso = controller.find_all_curso()

        print(all_curso)

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_update_curso(self, controller: CursosController):
        ultimoRegistro = controller.find_all_curso()
        ultimoRegistro = ultimoRegistro[-1]
        id = ultimoRegistro["id"]
        edit_curso = CursosInputDTO(
            ultimoRegistro["sistema"],
            ultimoRegistro["unidade"],
            "Catapimbas",
            ultimoRegistro["externalId"],
            ultimoRegistro["isActive"],
            ultimoRegistro["externalTeachingModalityId"],
            ultimoRegistro["externalEducationLevelId"],
            ultimoRegistro["courseTypeId"],
        )

        print(controller.update_curso(id, edit_curso))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_delete_(self, controller: CursosController):

        cursos = controller.find_all_curso()[-1]

        controller.delete_curso(cursos["id"])

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_export_cursos_CSV(self, controller: CursosController):
        controller.export_curso_to_CSV()
