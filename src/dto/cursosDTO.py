from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CursosInputDTO:
    sistema: str
    unidade: str
    name: str
    externalId: str
    isActive: bool
    externalTeachingModalityId: str
    externalEducationLevelId: str
    courseTypeId: str


@dataclass(frozen=True)
class CursosOutputDTO:
    id: int
    data: date
    sistema: str
    unidade: str
    name: str
    externalId: str
    isActive: bool
    externalTeachingModalityId: str
    externalEducationLevelId: str
    courseTypeId: str
