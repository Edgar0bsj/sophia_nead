from dataclasses import asdict
from src.models.cursos_model import CursosModel
from src.dto.cursosDTO import CursosOutputDTO
from typing import Any
import pandas as pd


class CursosService:

    def parseCurso(self, cursoInput: dict[str, str]) -> CursosModel:
        curso_model = CursosModel(
            sistema=cursoInput["sistema"],
            unidade=cursoInput["unidade"],
            name=cursoInput["name"],
            externalId=cursoInput["externalId"],
            isActive=cursoInput["isActive"],
            externalTeachingModalityId=cursoInput["externalTeachingModalityId"],
            externalEducationLevelId=cursoInput["externalEducationLevelId"],
            courseTypeId=cursoInput["courseTypeId"],
        )

        return curso_model

    def parseResponse(self, curso_model: CursosModel) -> CursosOutputDTO:
        curso_output = CursosOutputDTO(
            id=curso_model.id,
            data=curso_model.data,
            sistema=curso_model.sistema,
            unidade=curso_model.unidade,
            name=curso_model.name,
            externalId=curso_model.externalId,
            isActive=curso_model.isActive,
            externalTeachingModalityId=curso_model.externalTeachingModalityId,
            externalEducationLevelId=curso_model.externalEducationLevelId,
            courseTypeId=curso_model.courseTypeId,
        )

        return asdict(curso_output)

    def map_curso_to_dict(self, curso_array: list[CursosModel]) -> dict[str, Any]:
        cursos = []
        for idx in range(len(curso_array)):
            cursoOutput = CursosOutputDTO(
                curso_array[idx].id,
                curso_array[idx].data,
                curso_array[idx].sistema,
                curso_array[idx].unidade,
                curso_array[idx].name,
                curso_array[idx].externalId,
                curso_array[idx].isActive,
                curso_array[idx].externalTeachingModalityId,
                curso_array[idx].externalEducationLevelId,
                curso_array[idx].courseTypeId,
            )
            cursos.append(asdict(cursoOutput))
        return cursos

    def exportEntityToCSV(self, all_cursos: list[CursosModel]) -> None:
        entitys = [
            {
                "id": e.id,
                "data": e.data,
                "sistema": e.sistema,
                "unidade": e.unidade,
                "name": e.name,
                "externalId": e.externalId,
                "isActive": e.isActive,
                "externalTeachingModalityId": e.externalTeachingModalityId,
                "externalEducationLevelId": e.externalEducationLevelId,
                "courseTypeId": e.courseTypeId,
            }
            for e in all_cursos
        ]

        df = pd.DataFrame(entitys)
        df = df.drop(columns=["id", "data", "sistema", "unidade"])
        df.to_csv(
            "output/course.unig_producao.csv",
            index=False,
            sep=";",
            encoding="utf-8",
        )
