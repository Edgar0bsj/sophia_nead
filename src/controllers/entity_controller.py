from datetime import date

from src.services.entity_service import EntityService
from src.repositories.entitys_repository import EntityRepository
from src.dto.entityDTO import EntityInputDTO
from src.models.entitys_model import EntitysModel
from dataclasses import asdict


class EntityController:
    def __init__(self) -> None:
        self.repository = EntityRepository()
        self.service = EntityService()

    def create_entity(self, entity_input: EntityInputDTO):
        try:
            entity = asdict(entity_input)
            entity_model = self.service.parseEntity(entity)
            entity_save = self.repository.create(entity_model)
            response = self.service.parseResponse(entity_save)
            return response

        except Exception as err:
            print(err)
            raise

    def find_all_entity(self):
        try:
            all_entity = self.repository.find_all()
            response = self.service.map_entities_to_dict(all_entity)

            return response

        except Exception as err:
            print(err)
            raise

    def update_entity(self, id: int, entity_input: EntityInputDTO):
        try:
            entity = asdict(entity_input)
            entity_model = self.service.parseEntity(entity)
            newEntity = self.repository.update(id, entity_model)
            response = self.service.parseResponse(newEntity)
            return response
        except Exception as err:
            print(err)
            raise

    def delete_entity(self, id: int):
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

            self.service.exportEntityToCSV(all_entitys)

        except Exception as err:
            print(err)
            raise
