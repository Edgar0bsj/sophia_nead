from datetime import date

from src.services.modalidade_service import ModalidadeService
from src.repositories.modalidade_repository import ModalidadeRepository
from src.dto.modalidadeDTO import ModalidadeInputDTO
from src.models.modalidade_model import ModalidadeModel
from dataclasses import asdict


class ModalidadeController:
    def __init__(self) -> None:
        self.repository = ModalidadeRepository()
        self.service = ModalidadeService()

    def create_modalidade(self, modalidade_input: ModalidadeInputDTO):
        try:
            modalidade = asdict(modalidade_input)
            modalidade_model = self.service.parseModalidade(modalidade)
            modalidade_save = self.repository.create(modalidade_model)
            response = self.service.parseResponse(modalidade_save)
            return response

        except Exception as err:
            print(err)
            raise

    def find_all_modalidade(self):
        try:
            all_modalidade = self.repository.find_all()
            response = self.service.map_modalidade_to_dict(all_modalidade)

            return response

        except Exception as err:
            print(err)
            raise

    def update_modalidade(self, id: int, modalidade_input: ModalidadeInputDTO):
        try:
            modalidade = asdict(modalidade_input)
            modalidade_model = self.service.parseModalidade(modalidade)
            newModalidade = self.repository.update(id, modalidade_model)
            response = self.service.parseResponse(newModalidade)
            return response
        except Exception as err:
            print(err)
            raise

    def delete_modalidade(self, id: int):
        try:
            self.repository.delete(id)
        except Exception as err:
            print(err)
            raise

    def export_modalidade_to_CSV(self, data_filter=None):
        try:
            if data_filter is None:
                data_filter = date.today()

            all_modalidade = self.repository.find_by_data(data_filter)
            self.service.exportModalidadeToCSV(all_modalidade)

        except Exception as err:
            print(err)
            raise

    def get_cursos_by_modalidade(self, id: int):
        cursos = self.repository.list_cursos(id)
        cursos_dict = [
            {
                "id": x.id,
                "data": x.data,
                "sistema": x.sistema,
                "unidade": x.unidade,
                "name": x.name,
                "externalId": x.externalId,
                "isActive": x.isActive,
                "externalTeachingModalityId": x.externalTeachingModalityId,
                "externalEducationLevelId": x.externalEducationLevelId,
                "courseTypeId": x.courseTypeId,
            }
            for x in cursos
        ]
        print(cursos_dict)
