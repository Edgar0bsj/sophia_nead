from src.interface.service_interface import ServiceInterface
from src.models.nivelDeEnsino_model import NivelDeEnsinoModel


class NivelDeEnsinoController:
    def __init__(self, service: ServiceInterface) -> None:
        self.service = service

    def create_nivelDeEnsino(
        self, nivel_de_ensino_model: NivelDeEnsinoModel
    ) -> NivelDeEnsinoModel:
        try:

            return self.service.save(nivel_de_ensino_model)

        except Exception as err:
            print(err)

    def find_all_nivelDeEnsino(self) -> list[NivelDeEnsinoModel]:
        try:
            return self.service.find_all()

        except Exception as err:
            print(err)
            raise

    def find_by_id_nivelDeEnsino(self, id: int):
        try:
            return self.service.find_by_id(id)

        except Exception as err:
            print(err)
            raise

    def update_nivelDeEnsino(
        self, nivel_de_ensino_model: NivelDeEnsinoModel
    ) -> NivelDeEnsinoModel:
        try:
            return self.service.update(nivel_de_ensino_model)

        except Exception as err:
            print(err)
            raise

    def remove_nivelDeEnsino(self, id: int) -> NivelDeEnsinoModel:
        try:
            return self.service.delete(id)

        except Exception as err:
            print(err)
            raise
