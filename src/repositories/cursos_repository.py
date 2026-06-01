from typing import Optional

from sqlalchemy.orm import Session

from src.interface.repository_interface import RepositoryInterface
from src.models.cursos_model import CursosModel


class CursosRepository(RepositoryInterface[CursosModel]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, cursos_model: CursosModel) -> CursosModel:
        self.session.add(cursos_model)
        self.session.commit()

        return cursos_model

    def update(self, cursos_model: CursosModel) -> CursosModel:
        resultFind = (
            self.session.query(CursosModel)
            .filter(CursosModel.id == cursos_model.id)
            .first()
        )

        resultFind.sistema = cursos_model.sistema
        resultFind.unidade = cursos_model.unidade
        resultFind.cursos_name = cursos_model.cursos_name
        resultFind.externalId = cursos_model.externalId
        resultFind.isActive = cursos_model.isActive
        resultFind.externalTeachingModalityId = cursos_model.externalTeachingModalityId
        resultFind.externalEducationLevelId = cursos_model.externalEducationLevelId
        resultFind.courseTypeId = cursos_model.courseTypeId

        self.session.commit()
        return resultFind

    def find_all(self) -> list[CursosModel]:
        return self.session.query(CursosModel).all()

    def find_by_id(self, id: int) -> Optional[CursosModel]:

        return self.session.query(CursosModel).filter(CursosModel.id == id).first()

    def delete(self, id: int) -> Optional[CursosModel]:
        modalidade = (
            self.session.query(CursosModel).filter(CursosModel.id == id).first()
        )

        self.session.delete(modalidade)
        self.session.commit()

        return modalidade
