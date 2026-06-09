from datetime import date

from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.models.modalidade_model import ModalidadeModel
from typing import Any


class ModalidadeRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create(self, entitys_model: ModalidadeModel) -> ModalidadeModel:
        self.session.add(entitys_model)
        self.session.commit()
        return entitys_model

    def find_all(self) -> list[ModalidadeModel]:
        return self.session.query(ModalidadeModel).all()

    def update(
        self, _id: int, entitys_model: ModalidadeModel
    ) -> ModalidadeModel | None:
        newModalidade = self.session.query(ModalidadeModel).filter_by(id=_id).first()

        newModalidade.sistema = entitys_model.sistema
        newModalidade.unidade = entitys_model.unidade
        newModalidade.modalidade_nome = entitys_model.modalidade_nome
        newModalidade.externalId = entitys_model.externalId
        newModalidade.teachingModalityTypeId = entitys_model.teachingModalityTypeId

        self.session.commit()
        return newModalidade

    def delete(self, _id: int) -> ModalidadeModel | None:
        findModalidade = self.session.query(ModalidadeModel).filter_by(id=_id).first()
        self.session.delete(findModalidade)
        self.session.commit()
        return findModalidade

    def find_by_data(self, data: date) -> list[ModalidadeModel] | None:
        all_modalidade = (
            self.session.query(ModalidadeModel)
            .filter(ModalidadeModel.data == data)
            .all()
        )

        return all_modalidade

    def list_cursos(self, _id: int) -> list[Any]:
        father = self.session.query(ModalidadeModel).filter_by(id=_id).first()
        return father.cursos
