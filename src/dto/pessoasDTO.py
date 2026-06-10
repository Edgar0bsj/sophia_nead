from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class PessoasInputDTO:
    sistema: str
    unidade: str
    name: str
    socialName: str | None
    identityDocument: str
    identityDocumentTypeId: str
    passportNumber: str | None
    externalId: str
    address_zipCode: str | None
    address_state: str | None
    address_city: str | None
    address_address: str | None
    address_number: str | None
    address_neighborhood: str | None
    address_complement: str | None
    user_email: str
    user_username: str
    user_password: str
    tags: list | None


@dataclass(frozen=True)
class PessoasOutputDTO:
    id: int
    data: date
    sistema: str
    unidade: str
    name: str
    socialName: str | None
    identityDocument: str
    identityDocumentTypeId: str
    passportNumber: str | None
    externalId: str
    address_zipCode: str | None
    address_state: str | None
    address_city: str | None
    address_address: str | None
    address_number: str | None
    address_neighborhood: str | None
    address_complement: str | None
    user_email: str
    user_username: str
    user_password: str
    tags: list | None
