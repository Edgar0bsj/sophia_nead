from src.database.base import Base
from src.database.connection import engine

from src.models.entitys_model import EntitysModel

class Tables:
    def __init__(self):
        self.entity_polo = EntitysModel
        self.base = Base
        self.engine = engine
        
    
    def create_tables(self):
        return self.base.metadata.create_all(self.engine)