from datetime import date

from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.models.pessoa_model import PessoasModel


class PessoasRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create(self, pessoas_model: PessoasModel) -> PessoasModel:
        self.session.add(pessoas_model)
        self.session.commit()
        return pessoas_model

    def find_all(self) -> list[PessoasModel]:
        return self.session.query(PessoasModel).all()

    def update(self, _id: int, pessoas_model: PessoasModel) -> PessoasModel | None:
        newPessoa = self.session.query(PessoasModel).filter_by(id=_id).first()

        newPessoa.sistema = pessoas_model.sistema
        newPessoa.unidade = pessoas_model.unidade
        newPessoa.name = pessoas_model.name
        newPessoa.socialName = pessoas_model.socialName
        newPessoa.identityDocument = pessoas_model.identityDocument
        newPessoa.identityDocumentTypeId = pessoas_model.identityDocumentTypeId
        newPessoa.passportNumber = pessoas_model.passportNumber
        newPessoa.externalId = pessoas_model.externalId
        newPessoa.address_zipCode = pessoas_model.address_zipCode
        newPessoa.address_state = pessoas_model.address_state
        newPessoa.address_city = pessoas_model.address_city
        newPessoa.address_address = pessoas_model.address_address
        newPessoa.address_number = pessoas_model.address_number
        newPessoa.address_neighborhood = pessoas_model.address_neighborhood
        newPessoa.address_complement = pessoas_model.address_complement
        newPessoa.user_email = pessoas_model.user_email
        newPessoa.user_username = pessoas_model.user_username
        newPessoa.user_password = pessoas_model.user_password
        newPessoa.tags = pessoas_model.tags

        self.session.commit()
        return newPessoa

    def delete(self, _id: int) -> PessoasModel | None:
        findPessoa = self.session.query(PessoasModel).filter_by(id=_id).first()
        self.session.delete(findPessoa)
        self.session.commit()
        return findPessoa

    def find_by_data(self, data: date) -> list[PessoasModel] | None:
        all_pessoa = (
            self.session.query(PessoasModel).filter(PessoasModel.data == data).all()
        )

        return all_pessoa
