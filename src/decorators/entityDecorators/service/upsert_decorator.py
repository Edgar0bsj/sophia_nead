from functools import wraps
from src.dto.entityDTO import EntityDTO
from datetime import date
from src.interface.entityInterface.entity_service_interface import EntityServiceInterface

def UpsertDecorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        dto: EntityDTO = args[1]

        service:EntityServiceInterface = args[0]

        data_atual = date.today()

        entity_all = service.find_all_entity()

        for entity in entity_all:

            same_entity = (
                dto.entity_name == entity.entity_name and
                dto.unidade == entity.unidade and
                dto.sistema == entity.sistema and
                data_atual == entity.data
            )

            if not same_entity:
                continue

            entity.oldExternalId = dto.oldExternalId
            entity.newExternalId = dto.newExternalId

            return service.update_entity(entity)

        return func(*args, **kwargs)

    return wrapper