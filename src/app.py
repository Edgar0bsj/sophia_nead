import sys

from src.database.tables import Tables

from src.containers.entity_container import EntityContainer
from src.schemas.entitys_schema import EntitysInput

from src.views.home_page import HomePage
from PyQt6 import QtWidgets



class MainApp:
        def __init__(self)-> None:
              self.app = QtWidgets.QApplication(sys.argv)
              self.janela = HomePage()
              
        def boostrap(self):
                self.janela.show()
                sys.exit(self.app.exec())
                
                return None
        


if __name__ == "__main__":
    Tables().create_tables()
#     app = MainApp()
#     app.boostrap()
    
    entityService = EntityContainer.create()
    
    result = entityService.find_all_entity()
    
    print(entityService.find_by_id_entity(result[0].id))
    
#     entityService.create_entity(EntitysInput(
#           sistema="avalia",
#           entity_name="polo",
#           unidade="Nova Iguaçu",
#           oldExternalId="854563",
#           newExternalId="963258"
#     ))

