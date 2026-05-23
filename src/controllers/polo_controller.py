from src.services.polo_service import PoloService
from src.schemas.polo_schema import PoloInput

class PoloController:
    def __init__(self):
        self.service = PoloService()
        
        
        
        
    def create_polo(self, polo:PoloInput):
        return self.service.create_case(polo.nome)
    
    def find_all_polo(self):
        return self.service.find_all_case()
    
    def find_by_id_polo(self, id):
        return self.service.find_by_id_case(id)
    
    def update_polo(self, polo:PoloInput):
        return self.service.update_case(polo)
    
    def delete_polo(self, id):
        return self.service.delete_case(id)