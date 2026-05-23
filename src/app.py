from src.database.tables import Tables

from src.controllers.polo_controller import PoloController
from src.schemas.polo_schema import PoloInput


class MainApp:
    def __init__(self):
        self.tables = Tables()
        self.polo_controller = PoloController()
        
        self.tables.create_tables()
        
    
        
    def inicializar(self):

# ///////////////////////////////////////////////////
#                      CREATE POLO
# ///////////////////////////////////////////////////
        polo = PoloInput(nome='ItaperuNAN')
        #>>>> self.polo_controller.create_polo(polo)
        
# ///////////////////////////////////////////////////
#                      FIND ALL POLO
# ///////////////////////////////////////////////////
        poloss = self.polo_controller.find_all_polo()
        
# ///////////////////////////////////////////////////
#                      FIND BY ID POLO
# ///////////////////////////////////////////////////
        self.polo_controller.find_by_id_polo(poloss[0].id)
        
# ///////////////////////////////////////////////////
#                      EDIT POLO
# ///////////////////////////////////////////////////
        print(self.polo_controller.update_polo(PoloInput(
            id=poloss[1].id,
            nome="Catabolas"
        )))
        
# ///////////////////////////////////////////////////
#                      DELETE
# ///////////////////////////////////////////////////
        self.polo_controller.delete_polo(poloss[0].id)

# ///////////////////////////////////////////////////
#                   INICIALIZAÇÃO
# ///////////////////////////////////////////////////
if __name__ == "__main__":
    app = MainApp()
    app.inicializar()
    
    
