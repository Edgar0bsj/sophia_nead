from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class ModalidadeInputDTO:
    sistema: str
    unidade: str
    modalidade_nome: str
    externalId: str
    teachingModalityTypeId: str


@dataclass(frozen=True)
class ModalidadeOutputDTO:
    id: int
    data: date
    sistema: str
    unidade: str
    modalidade_nome: str
    externalId: str
    teachingModalityTypeId: str
