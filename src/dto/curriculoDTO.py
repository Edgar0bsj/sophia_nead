from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CurriculoInputDTO:
    sistema: str
    unidade: str
    externalCourseId: str
    name: str
    externalId: str
    workload: float
    startDate: date | None
    endDate: date | None
    isActive: bool


@dataclass(frozen=True)
class CurriculoOutputDTO:
    id: int
    data: date
    sistema: str
    unidade: str
    externalCourseId: str
    name: str
    externalId: str
    workload: float
    startDate: date | None
    endDate: date | None
    isActive: bool
