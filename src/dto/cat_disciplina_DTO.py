from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CategoriasDaDisciplinaInputDTO:
    sistema: str
    unidade: str
    name: str
    externalId: str
    subjectCategoryTypeId: str
    isActive: bool


@dataclass(frozen=True)
class CategoriasDaDisciplinaOutputDTO:
    id: int
    data: date
    sistema: str
    unidade: str
    name: str
    externalId: str
    subjectCategoryTypeId: str
    isActive: bool
