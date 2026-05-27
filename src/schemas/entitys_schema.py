from datetime import date

from pydantic import BaseModel
    
class EntitysInput(BaseModel):
    sistema: str
    entity_name:str
    unidade: str
    oldExternalId: str
    newExternalId: str
    data: date | None = None
    id: int | None = None