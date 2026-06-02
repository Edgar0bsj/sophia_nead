from typing import Optional

from sqlalchemy.orm import Session

from src.interface.repository_interface import RepositoryInterface
from src.models.curriculo_model import CurriculoModel


class CurriculoRepository(RepositoryInterface[CurriculoModel]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, curriculo_model: CurriculoModel) -> CurriculoModel:
        self.session.add(curriculo_model)
        self.session.commit()

        return curriculo_model

    def update(self, curriculo_model: CurriculoModel) -> CurriculoModel:
        resultFind = (
            self.session.query(CurriculoModel)
            .filter(CurriculoModel.id == curriculo_model.id)
            .first()
        )

        resultFind.sistema = curriculo_model.sistema
        resultFind.unidade = curriculo_model.unidade
        resultFind.externalCourseId = curriculo_model.externalCourseId
        resultFind.curriculo_name = curriculo_model.curriculo_name
        resultFind.externalId = curriculo_model.externalId
        resultFind.workload = curriculo_model.workload
        resultFind.startDate = curriculo_model.startDate
        resultFind.endDate = curriculo_model.endDate
        resultFind.isActive = curriculo_model.isActive

        self.session.commit()
        return resultFind

    def find_all(self) -> list[CurriculoModel]:
        return self.session.query(CurriculoModel).all()

    def find_by_id(self, id: int) -> Optional[CurriculoModel]:

        return (
            self.session.query(CurriculoModel).filter(CurriculoModel.id == id).first()
        )

    def delete(self, id: int) -> Optional[CurriculoModel]:
        resultFind = (
            self.session.query(CurriculoModel).filter(CurriculoModel.id == id).first()
        )

        self.session.delete(resultFind)
        self.session.commit()

        return resultFind
