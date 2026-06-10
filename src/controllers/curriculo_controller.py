from datetime import date

from src.services.curriculo_service import CurriculoService
from src.repositories.curriculo_repository import CurriculoRepository
from src.dto.curriculoDTO import CurriculoInputDTO
from dataclasses import asdict


class CurriculoController:
    def __init__(self) -> None:
        self.repository = CurriculoRepository()
        self.service = CurriculoService()

    def create_curriculo(self, curriculo_input: CurriculoInputDTO):
        try:
            curriculo = asdict(curriculo_input)
            curriculo_model = self.service.parseCurriculo(curriculo)
            curriculo_save = self.repository.create(curriculo_model)
            response = self.service.parseResponse(curriculo_save)
            return response

        except Exception as err:
            print(err)
            raise

    def find_all_curriculo(self):
        try:
            all_curriculo = self.repository.find_all()
            response = self.service.map_curriculo_to_dict(all_curriculo)

            return response

        except Exception as err:
            print(err)
            raise

    def update_curriculo(self, id: int, curriculo_input: CurriculoInputDTO):
        try:
            curriculo = asdict(curriculo_input)
            curriculo_model = self.service.parseCurriculo(curriculo)
            newCurriculo = self.repository.update(id, curriculo_model)
            response = self.service.parseResponse(newCurriculo)
            return response
        except Exception as err:
            print(err)
            raise

    def delete_curriculo(self, id: int):
        try:
            self.repository.delete(id)
        except Exception as err:
            print(err)
            raise

    def export_curriculo_to_CSV(self, data_filter=None):
        try:
            if data_filter is None:
                data_filter = date.today()

            all_curriculo = self.repository.find_by_data(data_filter)
            self.service.exportCurriculoToCSV(all_curriculo)

        except Exception as err:
            print(err)
            raise
