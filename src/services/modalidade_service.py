from src.interface.service_interface import ServiceInterface
from src.models.modalidade_model import ModalidadeModel
from src.interface.repository_interface import RepositoryInterface


class ModalidadeService(ServiceInterface[ModalidadeModel]):

    def __init__(self, modalidadeRepository: RepositoryInterface):
        self.repository = modalidadeRepository

    def find_by_id(self, id: int) -> ModalidadeModel:
        return self.repository.find_by_id(id)

    def find_all(self) -> list[ModalidadeModel]:
        return self.repository.find_all()

    def save(self, entitysInput: ModalidadeModel) -> ModalidadeModel:
        return self.repository.save(entitysInput)

    def update(self, entitysInput: ModalidadeModel) -> ModalidadeModel:
        return self.repository.update(entitysInput)

    def delete(self, id: int) -> ModalidadeModel:
        return self.repository.delete(id)
