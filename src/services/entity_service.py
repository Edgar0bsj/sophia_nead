from datetime import date

from src.repositories.entitys_repository import EntityRepository
from src.models.entitys_model import EntitysModel
from src.dto.entityDTO import EntityInputDTO


class EntityService:

    def __init__(self, entityRepository: EntityRepository):
        self.repository = entityRepository

    def create_entity(self, entityInput: EntityInputDTO) -> bool:

        parseEntity = EntitysModel(
            sistema=entityInput.sistema,
            unidade=entityInput.unidade,
            entity_name=entityInput.entity.value,
            oldExternalId=entityInput.oldExternalId,
            newExternalId=entityInput.newExternalId,
        )

        result = self.repository.save(parseEntity)

        if result is not None:
            return True
        else:
            return False

    def update_entity(self, id: int, entityInput: EntityInputDTO) -> bool:

        parseEntity = EntitysModel(
            sistema=entityInput.sistema,
            unidade=entityInput.unidade,
            entity_name=entityInput.entity.value,
            oldExternalId=entityInput.oldExternalId,
            newExternalId=entityInput.newExternalId,
        )

        result = self.repository.update(id, parseEntity)

        if result is not None:
            return True
        else:
            return False

    def find_all_entity(self):
        return self.repository.find_all()

    def find_entity(self, data: date, sistema: str, unidade: str):
        return self.repository.find(data, sistema, unidade)

    def delete_entity(self, id: int) -> bool:
        result = self.repository.delete(id)

        if result:
            return True
        else:
            return False
