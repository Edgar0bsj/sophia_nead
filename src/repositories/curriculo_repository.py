from datetime import date

from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.models.curriculo_model import CurriculoModel


class CurriculoRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create(self, curriculo_model: CurriculoModel) -> CurriculoModel:
        self.session.add(curriculo_model)
        self.session.commit()
        return curriculo_model

    def find_all(self) -> list[CurriculoModel]:
        return self.session.query(CurriculoModel).all()

    def update(
        self, _id: int, curriculo_model: CurriculoModel
    ) -> CurriculoModel | None:
        newCurriculo = self.session.query(CurriculoModel).filter_by(id=_id).first()

        newCurriculo.sistema = curriculo_model.sistema
        newCurriculo.unidade = curriculo_model.unidade
        newCurriculo.externalCourseId = curriculo_model.externalCourseId
        newCurriculo.name = curriculo_model.name
        newCurriculo.externalId = curriculo_model.externalId
        newCurriculo.workload = curriculo_model.workload
        newCurriculo.startDate = curriculo_model.startDate
        newCurriculo.endDate = curriculo_model.endDate
        newCurriculo.isActive = curriculo_model.isActive

        self.session.commit()
        return newCurriculo

    def delete(self, _id: int) -> CurriculoModel | None:
        findCurriculo = self.session.query(CurriculoModel).filter_by(id=_id).first()
        self.session.delete(findCurriculo)
        self.session.commit()
        return findCurriculo

    def find_by_data(self, data: date) -> list[CurriculoModel] | None:
        all_curriculo = (
            self.session.query(CurriculoModel).filter(CurriculoModel.data == data).all()
        )

        return all_curriculo
