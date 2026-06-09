from datetime import date

from src.services.niveis_de_ensino_service import NiveisDeEnsinoService
from src.repositories.niveis_de_ensino_repository import NiveisDeEnsinoRepository
from src.dto.niveis_de_ensinoDTO import NiveisDeEnsinoInputDTO
from dataclasses import asdict


class NiveisDeEnsinoController:
    def __init__(self) -> None:
        self.repository = NiveisDeEnsinoRepository()
        self.service = NiveisDeEnsinoService()

    def create_nvs_de_ensino(self, nvs_de_ensino_input: NiveisDeEnsinoInputDTO):
        try:
            nvs_de_ensino = asdict(nvs_de_ensino_input)
            nvs_de_ensino_model = self.service.parse_nvs_de_ensino(nvs_de_ensino)
            nvs_de_ensino_save = self.repository.create(nvs_de_ensino_model)
            response = self.service.parseResponse(nvs_de_ensino_save)
            return response

        except Exception as err:
            print(err)
            raise

    def find_all_nvs_de_ensino(self):
        try:
            all_nvs_de_ensino = self.repository.find_all()
            response = self.service.map_nvs_de_ensino_to_dict(all_nvs_de_ensino)

            return response

        except Exception as err:
            print(err)
            raise

    def update_nvs_de_ensino(
        self, id: int, nvs_de_ensino_input: NiveisDeEnsinoInputDTO
    ):
        try:
            nvs_de_ensino = asdict(nvs_de_ensino_input)
            nvs_de_ensino_model = self.service.parse_nvs_de_ensino(nvs_de_ensino)
            newNvs_de_ensino = self.repository.update(id, nvs_de_ensino_model)
            response = self.service.parseResponse(newNvs_de_ensino)
            return response
        except Exception as err:
            print(err)
            raise

    def delete_nvs_de_ensino(self, id: int):
        try:
            self.repository.delete(id)
        except Exception as err:
            print(err)
            raise

    def export_nvs_de_ensino_to_CSV(self, data_filter=None):
        try:
            if data_filter is None:
                data_filter = date.today()

            all_nvs_de_ensino = self.repository.find_by_data(data_filter)
            self.service.exportNvsDeEnsinoToCSV(all_nvs_de_ensino)

        except Exception as err:
            print(err)
            raise
