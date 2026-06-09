from dataclasses import asdict
from src.models.entitys_model import EntitysModel
from src.dto.entityDTO import EntityOutputDTO
from typing import Any
import pandas as pd


class EntityService:

    def parseEntity(self, entityInput: dict[str, str]) -> EntitysModel:
        entity_model = EntitysModel(
            sistema=entityInput["sistema"],
            unidade=entityInput["unidade"],
            entity_name=entityInput["entity_name"],
            oldExternalId=entityInput["oldExternalId"],
            newExternalId=entityInput["newExternalId"],
        )

        return entity_model

    def parseResponse(self, entitys_model: EntitysModel) -> EntityOutputDTO:
        entity_output = EntityOutputDTO(
            id=entitys_model.id,
            data=entitys_model.data,
            sistema=entitys_model.sistema,
            unidade=entitys_model.unidade,
            entity_name=entitys_model.entity_name,
            oldExternalId=entitys_model.oldExternalId,
            newExternalId=entitys_model.newExternalId,
        )

        return asdict(entity_output)

    def map_entities_to_dict(self, entity_array: list[EntitysModel]) -> dict[str, Any]:
        entitys = []
        for idx in range(len(entity_array)):
            entityOutput = EntityOutputDTO(
                entity_array[idx].id,
                entity_array[idx].data,
                entity_array[idx].sistema,
                entity_array[idx].unidade,
                entity_array[idx].entity_name,
                entity_array[idx].oldExternalId,
                entity_array[idx].newExternalId,
            )
            entitys.append(asdict(entityOutput))
        return entitys

    def exportEntityToCSV(self, all_entitys: list[EntitysModel]) -> None:
        entitys = [
            {
                "id": e.id,
                "data": e.data,
                "sistema": e.sistema,
                "unidade": e.unidade,
                "entity_name": e.entity_name,
                "oldExternalId": e.oldExternalId,
                "newExternalId": e.newExternalId,
            }
            for e in all_entitys
        ]

        df = pd.DataFrame(entitys)
        df = df.drop(columns=["id", "data", "sistema", "unidade"])
        df = df.rename(columns={"entity_name": "entity"})
        df.to_csv(
            "output/external-id-management.unig_producao.csv",
            index=False,
            sep=";",
            encoding="utf-8",
        )
