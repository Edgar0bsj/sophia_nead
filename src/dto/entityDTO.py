from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class EntityInputDTO:
    sistema: str
    unidade: str
    entity_name: str
    oldExternalId: str
    newExternalId: str


@dataclass(frozen=True)
class EntityOutputDTO:
    id: int
    data: date
    sistema: str
    unidade: str
    entity_name: str
    oldExternalId: str
    newExternalId: str
