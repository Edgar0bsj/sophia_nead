from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class NiveisDeEnsinoInputDTO:
    sistema: str
    unidade: str
    name: str
    externalId: str
    educationLevelTypeId: str


@dataclass(frozen=True)
class NiveisDeEnsinoOutputDTO:
    id: int
    data: date
    sistema: str
    unidade: str
    name: str
    externalId: str
    educationLevelTypeId: str
