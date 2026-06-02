from typing import Optional

from sqlalchemy.orm import Session

from src.models.pessoas_model import PessoasModel
from src.interface.repository_interface import RepositoryInterface


class PessoasRepository(RepositoryInterface[PessoasModel]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, pessoas_model: PessoasModel) -> PessoasModel:
        self.session.add(pessoas_model)
        self.session.commit()

        return pessoas_model

    def update(self, pessoas_model: PessoasModel) -> PessoasModel:
        resultFind = (
            self.session.query(PessoasModel)
            .filter(PessoasModel.id == pessoas_model.id)
            .first()
        )

        resultFind.sistema = pessoas_model.sistema
        resultFind.unidade = pessoas_model.unidade

        resultFind.pessoa_name = pessoas_model.pessoa_name
        resultFind.socialName = pessoas_model.socialName
        resultFind.identityDocument = pessoas_model.identityDocument
        resultFind.identityDocumentTypeId = pessoas_model.identityDocumentTypeId
        resultFind.passportNumber = pessoas_model.passportNumber
        resultFind.externalId = pessoas_model.externalId
        resultFind.address_zipCode = pessoas_model.address_zipCode
        resultFind.address_state = pessoas_model.address_state
        resultFind.address_city = pessoas_model.unidade
        resultFind.address_address = pessoas_model.address_address
        resultFind.address_number = pessoas_model.address_number
        resultFind.address_neighborhood = pessoas_model.address_neighborhood
        resultFind.address_complement = pessoas_model.address_complement
        resultFind.user_email = pessoas_model.user_email
        resultFind.user_username = pessoas_model.user_username
        resultFind.user_password = pessoas_model.user_password
        resultFind.tags = pessoas_model.tags

        self.session.commit()
        return resultFind

    def find_all(self) -> list[PessoasModel]:
        return self.session.query(PessoasModel).all()

    def find_by_id(self, id: int) -> Optional[PessoasModel]:

        return self.session.query(PessoasModel).filter(PessoasModel.id == id).first()

    def delete(self, id: int) -> Optional[PessoasModel]:
        resultFind = (
            self.session.query(PessoasModel).filter(PessoasModel.id == id).first()
        )

        self.session.delete(resultFind)
        self.session.commit()

        return resultFind
