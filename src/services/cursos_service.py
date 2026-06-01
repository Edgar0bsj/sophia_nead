from src.models.cursos_model import CursosModel
from src.interface.service_interface import ServiceInterface
from src.interface.repository_interface import RepositoryInterface


class CursosServices(ServiceInterface[RepositoryInterface]):

    def __init__(self, cursos_repository: RepositoryInterface):
        self.repository = cursos_repository

    def find_by_id(self, id: int) -> CursosModel:
        return self.repository.find_by_id(id)

    def find_all(self) -> list[CursosModel]:
        return self.repository.find_all()

    def save(self, cursos_model: CursosModel) -> CursosModel:
        return self.repository.save(cursos_model)

    def update(self, cursos_model: CursosModel) -> CursosModel:
        return self.repository.update(cursos_model)

    def delete(self, id: int) -> CursosModel:
        return self.repository.delete(id)
