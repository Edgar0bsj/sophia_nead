from dataclasses import asdict
from src.models.cat_disciplina_model import CategoriasDaDisciplinaModel
from src.dto.cat_disciplina_DTO import CategoriasDaDisciplinaOutputDTO
from typing import Any
import pandas as pd


class CategoriasDaDisciplinaService:

    def parse_catDiscip(
        self, cat_disciplina: dict[str, Any]
    ) -> CategoriasDaDisciplinaModel:
        catDiscip_model = CategoriasDaDisciplinaModel(
            sistema=cat_disciplina["sistema"],
            unidade=cat_disciplina["unidade"],
            name=cat_disciplina["name"],
            externalId=cat_disciplina["externalId"],
            subjectCategoryTypeId=cat_disciplina["subjectCategoryTypeId"],
            isActive=cat_disciplina["isActive"],
        )

        return catDiscip_model

    def parseResponse(
        self, catDiscip_model: CategoriasDaDisciplinaModel
    ) -> CategoriasDaDisciplinaOutputDTO:
        catDiscip_output = CategoriasDaDisciplinaOutputDTO(
            id=catDiscip_model.id,
            data=catDiscip_model.data,
            sistema=catDiscip_model.sistema,
            unidade=catDiscip_model.unidade,
            name=catDiscip_model.name,
            externalId=catDiscip_model.externalId,
            subjectCategoryTypeId=catDiscip_model.subjectCategoryTypeId,
            isActive=catDiscip_model.isActive,
        )

        return asdict(catDiscip_output)

    def map_catDiscip_to_dict(
        self, catDiscip_array: list[CategoriasDaDisciplinaModel]
    ) -> dict[str, Any]:
        catDisciplina = []
        for idx in range(len(catDiscip_array)):
            catDisciplinaOutput = CategoriasDaDisciplinaOutputDTO(
                catDiscip_array[idx].id,
                catDiscip_array[idx].data,
                catDiscip_array[idx].sistema,
                catDiscip_array[idx].unidade,
                catDiscip_array[idx].name,
                catDiscip_array[idx].externalId,
                catDiscip_array[idx].subjectCategoryTypeId,
                catDiscip_array[idx].isActive,
            )
            catDisciplina.append(asdict(catDisciplinaOutput))
        return catDisciplina

    def exportCatDiscipToCSV(
        self, all_cat_discip: list[CategoriasDaDisciplinaModel]
    ) -> None:
        car_discip = [
            {
                "id": e.id,
                "data": e.data,
                "sistema": e.sistema,
                "unidade": e.unidade,
                "name": e.name,
                "externalId": e.externalId,
                "subjectCategoryTypeId": e.subjectCategoryTypeId,
                "isActive": e.isActive,
            }
            for e in all_cat_discip
        ]

        df = pd.DataFrame(car_discip)
        df = df.drop(columns=["id", "data", "sistema", "unidade"])
        df = df.rename(columns={"entity_name": "entity"})
        df.to_csv(
            "output/subject-category.unig_producao.csv",
            index=False,
            sep=";",
            encoding="utf-8",
        )
