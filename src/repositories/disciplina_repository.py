from typing import Optional

from sqlalchemy.orm import Session

from src.interface.repository_interface import RepositoryInterface
from src.models.disciplinas_model import DisciplinasModel


class DisciplinaRepository(RepositoryInterface[DisciplinasModel]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, entity_model: DisciplinasModel) -> DisciplinasModel:
        self.session.add(entity_model)
        self.session.commit()

        return entity_model

    def update(self, entity_model: DisciplinasModel) -> DisciplinasModel:
        resultFind = (
            self.session.query(DisciplinasModel)
            .filter(DisciplinasModel.id == entity_model.id)
            .first()
        )

        resultFind.sistema = entity_model.sistema
        resultFind.unidade = entity_model.unidade
        resultFind.disciplina_name = entity_model.disciplina_name
        resultFind.externalId = entity_model.externalId
        resultFind.workload = entity_model.workload
        resultFind.isActive = entity_model.isActive
        resultFind.externalSubjectCategoryId = entity_model.externalSubjectCategoryId

        self.session.commit()
        return resultFind

    def find_all(self) -> list[DisciplinasModel]:
        return self.session.query(DisciplinasModel).all()

    def find_by_id(self, id: int) -> Optional[DisciplinasModel]:

        return (
            self.session.query(DisciplinasModel)
            .filter(DisciplinasModel.id == id)
            .first()
        )

    def delete(self, id: int) -> Optional[DisciplinasModel]:
        resultFind = (
            self.session.query(DisciplinasModel)
            .filter(DisciplinasModel.id == id)
            .first()
        )

        self.session.delete(resultFind)
        self.session.commit()

        return resultFind
