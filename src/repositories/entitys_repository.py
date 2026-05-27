from src.database.connection import SessionLocal
from src.models.entitys_model import EntitysModel
from src.schemas.entitys_schema import EntitysInput
from datetime import date

class EntityRepository:

    def __init__(self):
        self.session = SessionLocal()
        
    # ///////////////////////////////////////////////
    #               find_all
    # ///////////////////////////////////////////////
    def find_all(self)-> list[EntitysModel]:
        return (
            self.session
                .query(EntitysModel)
                .all()
                )

    # ///////////////////////////////////////////////
    #                   find_by_id
    # ///////////////////////////////////////////////
    def find_by_id(self, entity_id:int)-> EntitysModel:
        return (
            self.session
            .query(EntitysModel)
            .filter( EntitysModel.id == entity_id)
            .first()
        )
    
    # ///////////////////////////////////////////////
    #                   create
    # ///////////////////////////////////////////////
    def create(self, entityInput:EntitysInput)-> EntitysInput:

        entityOutput = EntitysModel(
            sistema=entityInput.sistema,
            unidade=entityInput.unidade,
            entity_name=entityInput.entity_name,
            oldExternalId=entityInput.oldExternalId,
            newExternalId=entityInput.newExternalId
        )

        self.session.add(entityOutput)
        self.session.commit()

        return entityOutput
    
    # ///////////////////////////////////////////////
    #                   update
    # ///////////////////////////////////////////////
    def update(self, entityInput:EntitysInput)-> EntitysInput:
        entityOutput = (
            self.session
            .query(EntitysModel)
            .filter(EntitysModel.id == entityInput.id)
            .first()
        )
        
        if not entityOutput: return None
        
        entityOutput.data = date.today()
        entityOutput.sistema = entityInput.sistema
        entityOutput.unidade = entityInput.unidade
        entityOutput.entity_name = entityInput.entity_name
        entityOutput.oldExternalId = entityInput.oldExternalId
        entityOutput.newExternalId = entityInput.newExternalId
        
        
        self.session.commit()
        self.session.refresh(entityOutput)
        
        return entityOutput
    
    # ///////////////////////////////////////////////
    #                   delete
    # ///////////////////////////////////////////////
    def delete(self, id:int)-> EntitysModel:
        
        entityOutput = (
            self.session
            .query(EntitysModel)
            .filter(EntitysModel.id == id)
            .first()
        )
        
        
        if not entityOutput: return False
        
        self.session.delete(entityOutput)
        self.session.commit()
        
        return entityOutput
        
        