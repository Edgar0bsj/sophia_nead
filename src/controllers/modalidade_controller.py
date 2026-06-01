from src.interface.service_interface import ServiceInterface
from src.models.modalidade_model import ModalidadeModel


class ModalidadeController:
    def __init__(self, service: ServiceInterface) -> None:
        self.service = service

    def create_modalidade(self, modalidade_model: ModalidadeModel) -> ModalidadeModel:
        try:

            return self.service.save(modalidade_model)

        except Exception as err:
            print(err)

    def find_all_modalidade(self) -> list[ModalidadeModel]:
        try:
            return self.service.find_all()

        except Exception as err:
            print(err)
            raise

    def find_by_id_modalidade(self, id: int):
        try:
            return self.service.find_by_id(id)

        except Exception as err:
            print(err)
            raise

    def update_modalidade(self, modalidade_model: ModalidadeModel) -> ModalidadeModel:
        try:
            return self.service.update(modalidade_model)

        except Exception as err:
            print(err)
            raise

    def remove_modalidade(self, id: int) -> ModalidadeModel:
        try:
            return self.service.delete(id)

        except Exception as err:
            print(err)
            raise
