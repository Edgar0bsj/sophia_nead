from src.repositories.polo_repository import PoloRepository
from src.schemas.polo_schema import PoloInput



class PoloService:
    def __init__(self):
        self.repository = PoloRepository()
        
        
    def create_case(self, name_polo):
        return self.repository.create(name_polo)
    
    def find_all_case(self):
        return self.repository.list_all()
    
    def find_by_id_case(self, id):
        return self.repository.get_by_id(id)
    
    def update_case(self, polo:PoloInput):
        return self.repository.update(**polo.__dict__)
    
    def delete_case(self, id):
        return self.repository.delete(id)