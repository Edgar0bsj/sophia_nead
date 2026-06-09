from dataclasses import asdict
from src.models.niveis_de_ensino_model import NiveisDeEnsinoModel
from src.dto.niveis_de_ensinoDTO import NiveisDeEnsinoOutputDTO
from typing import Any
import pandas as pd


class NiveisDeEnsinoService:

    def parse_nvs_de_ensino(
        self, nvs_de_ensinoInput: dict[str, str]
    ) -> NiveisDeEnsinoModel:
        nvs_de_ensino_model = NiveisDeEnsinoModel(
            sistema=nvs_de_ensinoInput["sistema"],
            unidade=nvs_de_ensinoInput["unidade"],
            name=nvs_de_ensinoInput["name"],
            externalId=nvs_de_ensinoInput["externalId"],
            educationLevelTypeId=nvs_de_ensinoInput["educationLevelTypeId"],
        )

        return nvs_de_ensino_model

    def parseResponse(
        self, nvs_de_ensino_model: NiveisDeEnsinoModel
    ) -> NiveisDeEnsinoOutputDTO:
        nvs_de_ensino_output = NiveisDeEnsinoOutputDTO(
            id=nvs_de_ensino_model.id,
            data=nvs_de_ensino_model.data,
            sistema=nvs_de_ensino_model.sistema,
            unidade=nvs_de_ensino_model.unidade,
            name=nvs_de_ensino_model.name,
            externalId=nvs_de_ensino_model.externalId,
            educationLevelTypeId=nvs_de_ensino_model.educationLevelTypeId,
        )

        return asdict(nvs_de_ensino_output)

    def map_nvs_de_ensino_to_dict(
        self, nvs_de_ensino_array: list[NiveisDeEnsinoModel]
    ) -> dict[str, Any]:
        nvs_de_ensino = []
        for idx in range(len(nvs_de_ensino_array)):
            nvs_de_ensinoOutput = NiveisDeEnsinoOutputDTO(
                nvs_de_ensino_array[idx].id,
                nvs_de_ensino_array[idx].data,
                nvs_de_ensino_array[idx].sistema,
                nvs_de_ensino_array[idx].unidade,
                nvs_de_ensino_array[idx].name,
                nvs_de_ensino_array[idx].externalId,
                nvs_de_ensino_array[idx].educationLevelTypeId,
            )
            nvs_de_ensino.append(asdict(nvs_de_ensinoOutput))
        return nvs_de_ensino

    def exportNvsDeEnsinoToCSV(
        self, all_nvs_de_ensino: list[NiveisDeEnsinoModel]
    ) -> None:
        nvs_de_ensino = [
            {
                "id": e.id,
                "data": e.data,
                "sistema": e.sistema,
                "unidade": e.unidade,
                "name": e.name,
                "externalId": e.externalId,
                "educationLevelTypeId": e.educationLevelTypeId,
            }
            for e in all_nvs_de_ensino
        ]

        df = pd.DataFrame(nvs_de_ensino)
        print(df.to_markdown(index=False))
        df = df.drop(columns=["id", "data", "sistema", "unidade"])
        df.to_csv(
            "output/education-level.unig_producao.csv",
            index=False,
            sep=";",
            encoding="utf-8",
        )
