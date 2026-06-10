from datetime import date

from src.services.pessoa_service import PessoaService
from src.repositories.pessoa_repository import PessoasRepository
from src.dto.pessoasDTO import PessoasInputDTO
from dataclasses import asdict


class PessoaController:
    def __init__(self) -> None:
        self.repository = PessoasRepository()
        self.service = PessoaService()

    def create_pessoa(self, pessoa_input: PessoasInputDTO):
        try:
            pessoa = asdict(pessoa_input)
            pessoa_model = self.service.parsePessoa(pessoa)
            pessoa_save = self.repository.create(pessoa_model)
            response = self.service.parseResponse(pessoa_save)
            return response

        except Exception as err:
            print(err)
            raise

    def find_all_pessoa(self):
        try:
            all_pessoa = self.repository.find_all()
            response = self.service.map_pessoa_to_dict(all_pessoa)

            return response

        except Exception as err:
            print(err)
            raise

    def update_pessoa(self, id: int, pessoa_input: PessoasInputDTO):
        try:
            pessoa = asdict(pessoa_input)
            pessoa_model = self.service.parsePessoa(pessoa)
            newPessoa = self.repository.update(id, pessoa_model)
            response = self.service.parseResponse(newPessoa)
            return response
        except Exception as err:
            print(err)
            raise

    def delete_pessoa(self, id: int):
        try:
            self.repository.delete(id)
        except Exception as err:
            print(err)
            raise

    def export_pessoa_to_CSV(self, data_filter=None):
        try:
            if data_filter is None:
                data_filter = date.today()

            all_pessoa = self.repository.find_by_data(data_filter)
            self.service.exportPessoaToCSV(all_pessoa)

        except Exception as err:
            print(err)
            raise
