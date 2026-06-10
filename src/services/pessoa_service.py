from dataclasses import asdict
from src.models.pessoa_model import PessoasModel
from src.dto.pessoasDTO import PessoasOutputDTO
from typing import Any
import pandas as pd


class PessoaService:

    def parsePessoa(self, pessoaInput: dict[str, str]) -> PessoasModel:
        pessoa_model = PessoasModel(
            sistema=pessoaInput["sistema"],
            unidade=pessoaInput["unidade"],
            name=pessoaInput["name"],
            socialName=pessoaInput["socialName"],
            identityDocument=pessoaInput["identityDocument"],
            identityDocumentTypeId=pessoaInput["identityDocumentTypeId"],
            passportNumber=pessoaInput["passportNumber"],
            externalId=pessoaInput["externalId"],
            address_zipCode=pessoaInput["address_zipCode"],
            address_state=pessoaInput["address_state"],
            address_city=pessoaInput["address_city"],
            address_address=pessoaInput["address_address"],
            address_number=pessoaInput["address_number"],
            address_neighborhood=pessoaInput["address_neighborhood"],
            address_complement=pessoaInput["address_complement"],
            user_email=pessoaInput["user_email"],
            user_username=pessoaInput["user_username"],
            user_password=pessoaInput["user_password"],
            tags=pessoaInput["tags"],
        )

        return pessoa_model

    def parseResponse(self, pessoa_model: PessoasModel) -> PessoasOutputDTO:
        pessoa_output = PessoasOutputDTO(
            id=pessoa_model.id,
            data=pessoa_model.data,
            sistema=pessoa_model.sistema,
            unidade=pessoa_model.unidade,
            name=pessoa_model.name,
            socialName=pessoa_model.socialName,
            identityDocument=pessoa_model.identityDocument,
            identityDocumentTypeId=pessoa_model.identityDocumentTypeId,
            passportNumber=pessoa_model.passportNumber,
            externalId=pessoa_model.externalId,
            address_zipCode=pessoa_model.address_zipCode,
            address_state=pessoa_model.address_state,
            address_city=pessoa_model.address_city,
            address_address=pessoa_model.address_address,
            address_number=pessoa_model.address_number,
            address_neighborhood=pessoa_model.address_neighborhood,
            address_complement=pessoa_model.address_complement,
            user_email=pessoa_model.user_email,
            user_username=pessoa_model.user_username,
            user_password=pessoa_model.user_password,
            tags=pessoa_model.tags,
        )

        return asdict(pessoa_output)

    def map_pessoa_to_dict(self, pessoa_array: list[PessoasModel]) -> dict[str, Any]:
        pessoa = []
        for idx in range(len(pessoa_array)):
            entityOutput = PessoasOutputDTO(
                pessoa_array[idx].id,
                pessoa_array[idx].data,
                pessoa_array[idx].sistema,
                pessoa_array[idx].unidade,
                pessoa_array[idx].name,
                pessoa_array[idx].socialName,
                pessoa_array[idx].identityDocument,
                pessoa_array[idx].identityDocumentTypeId,
                pessoa_array[idx].passportNumber,
                pessoa_array[idx].externalId,
                pessoa_array[idx].address_zipCode,
                pessoa_array[idx].address_state,
                pessoa_array[idx].address_city,
                pessoa_array[idx].address_address,
                pessoa_array[idx].address_number,
                pessoa_array[idx].address_neighborhood,
                pessoa_array[idx].address_complement,
                pessoa_array[idx].user_email,
                pessoa_array[idx].user_username,
                pessoa_array[idx].user_password,
                pessoa_array[idx].tags,
            )
            pessoa.append(asdict(entityOutput))
        return pessoa

    def exportPessoaToCSV(self, all_pessoa: list[PessoasModel]) -> None:
        pessoa = [
            {
                "id": e.id,
                "data": e.data,
                "sistema": e.sistema,
                "unidade": e.unidade,
                "name": e.name,
                "socialName": e.socialName,
                "identityDocument": e.identityDocument,
                "identityDocumentTypeId": e.identityDocumentTypeId,
                "passportNumber": e.passportNumber,
                "externalId": e.externalId,
                "address_zipCode": e.address_zipCode,
                "address_state": e.address_state,
                "address_city": e.address_city,
                "address_address": e.address_address,
                "address_number": e.address_number,
                "address_neighborhood": e.address_neighborhood,
                "address_complement": e.address_complement,
                "user_email": e.user_email,
                "user_username": e.user_username,
                "user_password": e.user_password,
                "tags": e.tags,
            }
            for e in all_pessoa
        ]

        df = pd.DataFrame(pessoa)
        df = df.drop(columns=["id", "data", "sistema", "unidade"])
        df = df.rename(
            columns={
                "address_zipCode": "address.zipCode",
                "address_state": "address.state",
                "address_city": "address.city",
                "address_address": "address.address",
                "address_number": "address.number",
                "address_neighborhood": "address.neighborhood",
                "address_complement": "address.complement",
                "user_email": "user.email",
                "user_username": "user.username",
                "user_password": "user.password",
            }
        )
        df.to_csv(
            "output/person.unig_producao.csv",
            index=False,
            sep=";",
            encoding="utf-8",
        )
