from datetime import date
from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class EntityDTO:
    sistema:str
    unidade:str
    entity_name:str
    oldExternalId:str
    newExternalId:str
    id:Optional[int] = None
    data:Optional[date] = None