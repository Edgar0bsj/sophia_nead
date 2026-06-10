from datetime import date

from src.services.cat_disciplina_service import CategoriasDaDisciplinaService
from src.repositories.cat_disciplina_repository import CategoriasDaDisciplinaRepository
from src.dto.cat_disciplina_DTO import CategoriasDaDisciplinaInputDTO
from dataclasses import asdict


class CategoriasDaDisciplinaController:
    def __init__(self) -> None:
        self.repository = CategoriasDaDisciplinaRepository()
        self.service = CategoriasDaDisciplinaService()

    def create_cat_disciplina(
        self, cat_disciplina_input: CategoriasDaDisciplinaInputDTO
    ):
        try:
            cat_dicisp = asdict(cat_disciplina_input)
            cat_discip_model = self.service.parse_catDiscip(cat_dicisp)
            cat_discip_save = self.repository.create(cat_discip_model)
            response = self.service.parseResponse(cat_discip_save)
            return response

        except Exception as err:
            print(err)
            raise

    def find_all_catDiscip(self):
        try:
            all_cat_discip = self.repository.find_all()
            response = self.service.map_catDiscip_to_dict(all_cat_discip)

            return response

        except Exception as err:
            print(err)
            raise

    def update_catDiscip(self, id: int, entity_input: CategoriasDaDisciplinaInputDTO):
        try:
            cat_discip = asdict(entity_input)
            cat_discip_model = self.service.parse_catDiscip(cat_discip)
            new_catDiscip = self.repository.update(id, cat_discip_model)
            response = self.service.parseResponse(new_catDiscip)
            return response
        except Exception as err:
            print(err)
            raise

    def delete_cat_discip(self, id: int):
        try:
            self.repository.delete(id)
        except Exception as err:
            print(err)
            raise

    def export_entity_to_CSV(self, data_filter=None):
        try:
            if data_filter is None:
                data_filter = date.today()

            all_entitys = self.repository.find_by_data(data_filter)
            self.service.exportCatDiscipToCSV(all_entitys)

        except Exception as err:
            print(err)
            raise
