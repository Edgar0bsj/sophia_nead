from datetime import date

from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.models.niveis_de_ensino_model import NiveisDeEnsinoModel


class NiveisDeEnsinoRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create(
        self, niveis_de_ensino_model: NiveisDeEnsinoModel
    ) -> NiveisDeEnsinoModel:
        self.session.add(niveis_de_ensino_model)
        self.session.commit()
        return niveis_de_ensino_model

    def find_all(self) -> list[NiveisDeEnsinoModel]:
        return self.session.query(NiveisDeEnsinoModel).all()

    def update(
        self, _id: int, niveis_de_ensino_model: NiveisDeEnsinoModel
    ) -> NiveisDeEnsinoModel | None:
        newNiveis_de_ensino = (
            self.session.query(NiveisDeEnsinoModel).filter_by(id=_id).first()
        )

        newNiveis_de_ensino.sistema = niveis_de_ensino_model.sistema
        newNiveis_de_ensino.unidade = niveis_de_ensino_model.unidade
        newNiveis_de_ensino.name = niveis_de_ensino_model.name
        newNiveis_de_ensino.externalId = niveis_de_ensino_model.externalId
        newNiveis_de_ensino.educationLevelTypeId = (
            niveis_de_ensino_model.educationLevelTypeId
        )

        self.session.commit()
        return newNiveis_de_ensino

    def delete(self, _id: int) -> NiveisDeEnsinoModel | None:
        findNiveis_de_ensino = (
            self.session.query(NiveisDeEnsinoModel).filter_by(id=_id).first()
        )
        self.session.delete(findNiveis_de_ensino)
        self.session.commit()
        return findNiveis_de_ensino

    def find_by_data(self, data: date) -> list[NiveisDeEnsinoModel] | None:
        all_niveis_de_ensino = (
            self.session.query(NiveisDeEnsinoModel)
            .filter(NiveisDeEnsinoModel.data == data)
            .all()
        )

        return all_niveis_de_ensino
