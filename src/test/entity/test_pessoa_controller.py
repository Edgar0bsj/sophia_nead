from datetime import date

import pytest

from src.dto.pessoasDTO import PessoasInputDTO
from src.controllers.pessoa_controller import PessoaController


@pytest.fixture
def controller():
    controller = PessoaController()
    return controller


class TestPessoaController:

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_create_pessoa(self, controller: PessoaController):
        pessoa_input = PessoasInputDTO(
            sistema="SOPHIA",
            unidade="NOVA IGUAÇU",
            name="Adriana Garces Guilherme",
            socialName=None,
            identityDocument="10186090757",
            identityDocumentTypeId="CPF",
            passportNumber=None,
            externalId="10186090757",
            address_zipCode=None,
            address_state=None,
            address_city=None,
            address_address=None,
            address_number=None,
            address_neighborhood=None,
            address_complement=None,
            user_email="drikasgarces@gmail.com",
            user_username="721014656",
            user_password="paisandu",
            tags=["UNIG", "2 Entrada"],
        )

        print(controller.create_pessoa(pessoa_input))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_find_all_pessoa(self, controller: PessoaController):
        all_pessoa = controller.find_all_pessoa()

        print(all_pessoa)

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_update_pessoa(self, controller: PessoaController):
        ultimoRegistro = controller.find_all_pessoa()
        ultimoRegistro = ultimoRegistro[-1]
        id = ultimoRegistro["id"]
        edit_pessoa = PessoasInputDTO(
            ultimoRegistro["sistema"],
            ultimoRegistro["unidade"],
            ultimoRegistro["name"],
            ultimoRegistro["socialName"],
            ultimoRegistro["identityDocument"],
            ultimoRegistro["identityDocumentTypeId"],
            ultimoRegistro["passportNumber"],
            ultimoRegistro["externalId"],
            ultimoRegistro["address_zipCode"],
            ultimoRegistro["address_state"],
            ultimoRegistro["address_city"],
            ultimoRegistro["address_address"],
            ultimoRegistro["address_number"],
            ultimoRegistro["address_neighborhood"],
            ultimoRegistro["address_complement"],
            ultimoRegistro["user_email"],
            ultimoRegistro["user_username"],
            ultimoRegistro["user_password"],
            ["UNIG", "3 Entrada"],
        )

        print(controller.update_pessoa(id, edit_pessoa))

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_delete_pessoa(self, controller: PessoaController):

        pessoa = controller.find_all_pessoa()[-1]

        controller.delete_pessoa(pessoa["id"])

    @pytest.mark.skip(reason="Ignorando temporariamente este teste")
    def test_export_pessoa_CSV(self, controller: PessoaController):
        controller.export_pessoa_to_CSV()
