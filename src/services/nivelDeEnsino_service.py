from src.interface.service_interface import ServiceInterface
from src.models.nivelDeEnsino_model import NivelDeEnsinoModel
from src.interface.repository_interface import RepositoryInterface


class NivelDeEnsinoService(ServiceInterface[NivelDeEnsinoModel]):

    def __init__(self, nivel_de_ensino_repository: RepositoryInterface):
        self.repository = nivel_de_ensino_repository

    def find_by_id(self, id: int) -> NivelDeEnsinoModel:
        return self.repository.find_by_id(id)

    def find_all(self) -> list[NivelDeEnsinoModel]:
        return self.repository.find_all()

    def save(self, nivel_de_ensino_model: NivelDeEnsinoModel) -> NivelDeEnsinoModel:
        return self.repository.save(nivel_de_ensino_model)

    def update(self, nivel_de_ensino_model: NivelDeEnsinoModel) -> NivelDeEnsinoModel:
        return self.repository.update(nivel_de_ensino_model)

    def delete(self, id: int) -> NivelDeEnsinoModel:
        return self.repository.delete(id)
