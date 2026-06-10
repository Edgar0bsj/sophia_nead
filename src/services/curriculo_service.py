from dataclasses import asdict
from src.models.curriculo_model import CurriculoModel
from src.dto.curriculoDTO import CurriculoOutputDTO
from typing import Any
import pandas as pd


class CurriculoService:

    def parseCurriculo(self, curriculoInput: dict[str, str]) -> CurriculoModel:
        curriculo_model = CurriculoModel(
            sistema=curriculoInput["sistema"],
            unidade=curriculoInput["unidade"],
            externalCourseId=curriculoInput["externalCourseId"],
            name=curriculoInput["name"],
            externalId=curriculoInput["externalId"],
            workload=curriculoInput["workload"],
            startDate=curriculoInput["startDate"],
            endDate=curriculoInput["endDate"],
            isActive=curriculoInput["isActive"],
        )

        return curriculo_model

    def parseResponse(self, curriculo_model: CurriculoModel) -> CurriculoOutputDTO:
        curriculo_output = CurriculoOutputDTO(
            id=curriculo_model.id,
            data=curriculo_model.data,
            sistema=curriculo_model.sistema,
            unidade=curriculo_model.unidade,
            externalCourseId=curriculo_model.externalCourseId,
            name=curriculo_model.name,
            externalId=curriculo_model.externalId,
            workload=curriculo_model.workload,
            startDate=curriculo_model.startDate,
            endDate=curriculo_model.endDate,
            isActive=curriculo_model.isActive,
        )

        return asdict(curriculo_output)

    def map_curriculo_to_dict(
        self, curriculo_array: list[CurriculoModel]
    ) -> dict[str, Any]:
        curriculo = []
        for idx in range(len(curriculo_array)):
            curriculoOutput = CurriculoOutputDTO(
                curriculo_array[idx].id,
                curriculo_array[idx].data,
                curriculo_array[idx].sistema,
                curriculo_array[idx].unidade,
                curriculo_array[idx].externalCourseId,
                curriculo_array[idx].name,
                curriculo_array[idx].externalId,
                curriculo_array[idx].workload,
                curriculo_array[idx].startDate,
                curriculo_array[idx].endDate,
                curriculo_array[idx].isActive,
            )
            curriculo.append(asdict(curriculoOutput))
        return curriculo

    def exportCurriculoToCSV(self, all_curriculo: list[CurriculoModel]) -> None:

        curriculos = [
            {
                "id": e.id,
                "data": e.data,
                "sistema": e.sistema,
                "unidade": e.unidade,
                "externalCourseId": e.externalCourseId,
                "name": e.name,
                "externalId": e.externalId,
                "workload": e.workload,
                "startDate": e.startDate,
                "endDate": e.endDate,
                "isActive": e.isActive,
            }
            for e in all_curriculo
        ]

        df = pd.DataFrame(curriculos)
        df = df.drop(columns=["id", "data", "sistema", "unidade"])
        print(df.to_markdown(index=False))
        df.to_csv(
            "output/curriculum.unig_producao.csv",
            index=False,
            sep=";",
            encoding="utf-8",
        )
