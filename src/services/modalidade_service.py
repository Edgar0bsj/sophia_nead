from dataclasses import asdict
from src.models.modalidade_model import ModalidadeModel
from src.dto.modalidadeDTO import ModalidadeOutputDTO
from typing import Any
import pandas as pd


class ModalidadeService:

    def parseModalidade(self, modalidade_input: dict[str, str]) -> ModalidadeModel:
        modalidade_model = ModalidadeModel(
            sistema=modalidade_input["sistema"],
            unidade=modalidade_input["unidade"],
            modalidade_nome=modalidade_input["modalidade_nome"],
            externalId=modalidade_input["externalId"],
            teachingModalityTypeId=modalidade_input["teachingModalityTypeId"],
        )

        return modalidade_model

    def parseResponse(self, modalidade_model: ModalidadeModel) -> ModalidadeOutputDTO:
        modalidade_output = ModalidadeOutputDTO(
            id=modalidade_model.id,
            data=modalidade_model.data,
            sistema=modalidade_model.sistema,
            unidade=modalidade_model.unidade,
            modalidade_nome=modalidade_model.modalidade_nome,
            externalId=modalidade_model.externalId,
            teachingModalityTypeId=modalidade_model.teachingModalityTypeId,
        )

        return asdict(modalidade_output)

    def map_modalidade_to_dict(
        self, modalidade_array: list[ModalidadeModel]
    ) -> dict[str, Any]:
        modalidade = []
        for idx in range(len(modalidade_array)):
            modalidadeOutput = ModalidadeOutputDTO(
                modalidade_array[idx].id,
                modalidade_array[idx].data,
                modalidade_array[idx].sistema,
                modalidade_array[idx].unidade,
                modalidade_array[idx].modalidade_nome,
                modalidade_array[idx].externalId,
                modalidade_array[idx].teachingModalityTypeId,
            )
            modalidade.append(asdict(modalidadeOutput))
        return modalidade

    def exportModalidadeToCSV(self, all_modalidade: list[ModalidadeModel]) -> None:
        modalidades = [
            {
                "id": e.id,
                "data": e.data,
                "sistema": e.sistema,
                "unidade": e.unidade,
                "modalidade_nome": e.modalidade_nome,
                "externalId": e.externalId,
                "teachingModalityTypeId": e.teachingModalityTypeId,
            }
            for e in all_modalidade
        ]

        df = pd.DataFrame(modalidades)

        df = df.drop(columns=["id", "data", "sistema", "unidade"])
        df = df.rename(columns={"modalidade_nome": "name"})
        df.to_csv(
            "output/teaching-modality.unig_producao.csv",
            index=False,
            sep=";",
            encoding="utf-8",
        )
