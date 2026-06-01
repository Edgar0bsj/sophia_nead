from typing import Optional

from sqlalchemy.orm import Session

from src.interface.repository_interface import RepositoryInterface
from src.models.modalidade_model import ModalidadeModel


class ModalidadeRepository(RepositoryInterface[ModalidadeModel]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, modalidade: ModalidadeModel) -> ModalidadeModel:
        self.session.add(modalidade)
        self.session.commit()

        return modalidade

    def update(self, modalidade: ModalidadeModel) -> ModalidadeModel:
        resultFind = (
            self.session.query(ModalidadeModel)
            .filter(ModalidadeModel.id == modalidade.id)
            .first()
        )

        resultFind.sistema = modalidade.sistema
        resultFind.unidade = modalidade.unidade
        resultFind.modalidade_nome = modalidade.modalidade_nome
        resultFind.externalId = modalidade.externalId
        resultFind.teachingModalityTypeId = modalidade.teachingModalityTypeId

        self.session.commit()
        return resultFind

    def find_all(self) -> list[ModalidadeModel]:
        return self.session.query(ModalidadeModel).all()

    def find_by_id(self, id: int) -> Optional[ModalidadeModel]:

        return (
            self.session.query(ModalidadeModel).filter(ModalidadeModel.id == id).first()
        )

    def delete(self, id: int) -> Optional[ModalidadeModel]:
        modalidade = (
            self.session.query(ModalidadeModel).filter(ModalidadeModel.id == id).first()
        )

        self.session.delete(modalidade)
        self.session.commit()

        return modalidade
