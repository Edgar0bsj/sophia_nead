from src.database.connection import SessionLocal
from src.models.polo_models import Polo

class PoloRepository:

    def __init__(self):
        self.session = SessionLocal()
        self.entity = Polo
        
    # ///////////////////////////////////////////////
    #               list_all
    # ///////////////////////////////////////////////
    def list_all(self):
       
        return self.session.query(self.entity).all()

    # ///////////////////////////////////////////////
    #                   get_by_id
    # ///////////////////////////////////////////////
    def get_by_id(self, polo_id):
        result = self.session.query(self.entity).filter(
            self.entity.id == polo_id
        ).first()
        
        return result
    
    # ///////////////////////////////////////////////
    #                   create
    # ///////////////////////////////////////////////
    def create(self, nome):

        polo = self.entity(
            nome=nome
        )

        self.session.add(polo)
        self.session.commit()
        self.session.refresh(polo)

        return polo
    
    # ///////////////////////////////////////////////
    #                   update
    # ///////////////////////////////////////////////
    def update(self, id, nome):
        polo = self.session.query(self.entity).filter(
            self.entity.id ==id
        ).first()
        
        if not polo: return None
        
        polo.nome = nome
        
        self.session.commit()
        self.session.refresh(polo)
        
        return polo
    
    # ///////////////////////////////////////////////
    #                   delete
    # ///////////////////////////////////////////////
    def delete(self, polo_id):
        
        polo = self.session.query(self.entity).filter(
            self.entity.id == polo_id
        ).first()
        
        if not polo: return False
        
        self.session.delete(polo)
        self.session.commit()
        
        return True
        
        