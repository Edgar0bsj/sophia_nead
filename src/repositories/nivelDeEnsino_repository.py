from typing import Optional

from sqlalchemy.orm import Session

from src.interface.repository_interface import RepositoryInterface
from src.models.nivelDeEnsino_model import NivelDeEnsinoModel


class NivelDeEnsinoRepository(RepositoryInterface[NivelDeEnsinoModel]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, nivel_de_ensino_model: NivelDeEnsinoModel) -> NivelDeEnsinoModel:
        self.session.add(nivel_de_ensino_model)
        self.session.commit()

        return nivel_de_ensino_model

    def update(self, nivel_de_ensino_model: NivelDeEnsinoModel) -> NivelDeEnsinoModel:
        resultFind = (
            self.session.query(NivelDeEnsinoModel)
            .filter(NivelDeEnsinoModel.id == nivel_de_ensino_model.id)
            .first()
        )

        resultFind.sistema = nivel_de_ensino_model.sistema
        resultFind.unidade = nivel_de_ensino_model.unidade
        resultFind.NivelDeEnsino_name = nivel_de_ensino_model.NivelDeEnsino_name
        resultFind.externalId = nivel_de_ensino_model.externalId
        resultFind.educationLevelTypeId = nivel_de_ensino_model.educationLevelTypeId

        self.session.commit()
        return resultFind

    def find_all(self) -> list[NivelDeEnsinoModel]:
        return self.session.query(NivelDeEnsinoModel).all()

    def find_by_id(self, id: int) -> Optional[NivelDeEnsinoModel]:

        return (
            self.session.query(NivelDeEnsinoModel)
            .filter(NivelDeEnsinoModel.id == id)
            .first()
        )

    def delete(self, id: int) -> Optional[NivelDeEnsinoModel]:
        modalidade = (
            self.session.query(NivelDeEnsinoModel)
            .filter(NivelDeEnsinoModel.id == id)
            .first()
        )

        self.session.delete(modalidade)
        self.session.commit()

        return modalidade
