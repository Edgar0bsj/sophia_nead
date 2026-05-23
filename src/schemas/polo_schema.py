from pydantic import BaseModel
    
class PoloInput(BaseModel):
    nome: str
    id:int = None