from datetime import date

from src.services.cursos_service import CursosService
from src.repositories.cursos_repository import CursosRepository
from src.dto.cursosDTO import CursosInputDTO
from dataclasses import asdict


class CursosController:
    def __init__(self) -> None:
        self.repository = CursosRepository()
        self.service = CursosService()

    def create_curso(self, curso_input: CursosInputDTO):
        try:
            curso = asdict(curso_input)
            curso_model = self.service.parseCurso(curso)
            curso_save = self.repository.create(curso_model)
            response = self.service.parseResponse(curso_save)
            return response

        except Exception as err:
            print(err)
            raise

    def find_all_curso(self):
        try:
            all_curso = self.repository.find_all()
            response = self.service.map_curso_to_dict(all_curso)

            return response

        except Exception as err:
            print(err)
            raise

    def update_curso(self, id: int, curso_input: CursosInputDTO):
        try:
            curso = asdict(curso_input)
            curso_model = self.service.parseCurso(curso)
            newCurso = self.repository.update(id, curso_model)
            response = self.service.parseResponse(newCurso)
            return response
        except Exception as err:
            print(err)
            raise

    def delete_curso(self, id: int):
        try:
            self.repository.delete(id)
        except Exception as err:
            print(err)
            raise

    def export_curso_to_CSV(self, data_filter=None):
        try:
            if data_filter is None:
                data_filter = date.today()

            all_entitys = self.repository.find_by_data(data_filter)
            self.service.exportEntityToCSV(all_entitys)

        except Exception as err:
            print(err)
            raise
