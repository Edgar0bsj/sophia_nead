from typing import Optional

from sqlalchemy.orm import Session

from src.interface.repository_interface import RepositoryInterface
from src.models.categoriasDaDisciplina_model import CategoriasDaDiciplinaModel


class CategoriasDaDisciplinaRepository(RepositoryInterface[CategoriasDaDiciplinaModel]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(
        self, categoria_model: CategoriasDaDiciplinaModel
    ) -> CategoriasDaDiciplinaModel:
        self.session.add(categoria_model)
        self.session.commit()

        return categoria_model

    def update(
        self, categoria_model: CategoriasDaDiciplinaModel
    ) -> CategoriasDaDiciplinaModel:
        resultFind = (
            self.session.query(CategoriasDaDiciplinaModel)
            .filter(CategoriasDaDiciplinaModel.id == categoria_model.id)
            .first()
        )

        resultFind.sistema = categoria_model.sistema
        resultFind.unidade = categoria_model.unidade
        resultFind.categoria_da_diciplina_name = (
            categoria_model.categoria_da_diciplina_name
        )
        resultFind.externalId = categoria_model.externalId
        resultFind.subjectCategoryTypeId = categoria_model.subjectCategoryTypeId
        resultFind.isActive = categoria_model.isActive

        self.session.commit()
        return resultFind

    def find_all(self) -> list[CategoriasDaDiciplinaModel]:
        return self.session.query(CategoriasDaDiciplinaModel).all()

    def find_by_id(self, id: int) -> Optional[CategoriasDaDiciplinaModel]:

        return (
            self.session.query(CategoriasDaDiciplinaModel)
            .filter(CategoriasDaDiciplinaModel.id == id)
            .first()
        )

    def delete(self, id: int) -> Optional[CategoriasDaDiciplinaModel]:
        resultFind = (
            self.session.query(CategoriasDaDiciplinaModel)
            .filter(CategoriasDaDiciplinaModel.id == id)
            .first()
        )

        self.session.delete(resultFind)
        self.session.commit()

        return resultFind
