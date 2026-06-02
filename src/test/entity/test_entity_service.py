from datetime import date

import pytest

from src.database.database_connection import DatabaseConnection
from src.dto.entityDTO import EntityInputDTO, EntityEnum
from src.services.entity_service import EntityService
from src.repositories.entitys_repository import EntityRepository


@pytest.fixture
def service():
    session = DatabaseConnection().bootstrap("sqlite:///:memory:")
    repository = EntityRepository(session())

    service = EntityService(repository)
    return service


@pytest.fixture
def entityInput_DTO():
    return EntityInputDTO(
        sistema="SOPHIA",
        unidade="UNIG",
        entity=EntityEnum.MATRICULAS,
        oldExternalId="123456789",
        newExternalId="987654321",
    )


class TestEntityService:

    def test_create_entity(
        self, service: EntityService, entityInput_DTO: EntityInputDTO
    ):

        result = service.create_entity(entityInput_DTO)

        assert result is not None
        assert result

    def test_update_entity(
        self, service: EntityService, entityInput_DTO: EntityInputDTO
    ):
        created = service.create_entity(entityInput_DTO)

        editEntity = EntityInputDTO(
            sistema="SOPHIA",
            unidade="ITAPERUNA",
            entity=EntityEnum.PESSOAS,
            oldExternalId="123",
            newExternalId="321",
        )

        result = service.update_entity(id=1, entityInput=editEntity)

        assert result is not None
        assert result

    def test_find_all_entity(
        self, service: EntityService, entityInput_DTO: EntityInputDTO
    ):

        created = service.create_entity(entityInput_DTO)
        result = service.find_all_entity()

        assert result is not None
        assert len(result) == 1
        assert result[0].entity_name == entityInput_DTO.entity.value
        assert created is True

    def test_find(self, service: EntityService, entityInput_DTO: EntityInputDTO):

        created = service.create_entity(entityInput_DTO)
        result = service.find_entity(date.today(), None, None)

        assert result is not None
        assert len(result) == 1
        assert result[0].entity_name == entityInput_DTO.entity.value
        assert created is True

    def test_delete_entity(
        self, service: EntityService, entityInput_DTO: EntityInputDTO
    ):

        created = service.create_entity(entityInput_DTO)
        result = service.find_entity(date.today(), None, None)

        resultDelet = service.delete_entity(result[0].id)

        assert resultDelet is not None
        assert len(result) >= 1
        assert resultDelet is True
