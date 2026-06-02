from sqlalchemy.orm import Session
from sqlalchemy import select

from src.models.entitys_model import EntitysModel
from datetime import date


class EntityRepository:

    def __init__(self, session: Session) -> None:

        self.session = session

    # ///////////////////////////////////////////////
    #               find_all
    # ///////////////////////////////////////////////
    def find_all(self) -> list[EntitysModel]:
        return self.session.query(EntitysModel).all()

    # ///////////////////////////////////////////////
    #                   find_by_id
    # ///////////////////////////////////////////////
    def find_by_id(self, entity_id: int) -> EntitysModel:
        return (
            self.session.query(EntitysModel)
            .filter(EntitysModel.id == entity_id)
            .first()
        )

    # ///////////////////////////////////////////////
    #                   create
    # ///////////////////////////////////////////////
    def save(self, entityInput: EntitysModel) -> EntitysModel:

        entityOutput = EntitysModel(
            sistema=entityInput.sistema,
            unidade=entityInput.unidade,
            entity_name=entityInput.entity_name,
            oldExternalId=entityInput.oldExternalId,
            newExternalId=entityInput.newExternalId,
        )

        self.session.add(entityOutput)
        self.session.commit()

        return entityOutput

    # ///////////////////////////////////////////////
    #                   update
    # ///////////////////////////////////////////////
    def update(self, id: int, entityInput: EntitysModel) -> EntitysModel:
        entityOutput = (
            self.session.query(EntitysModel).filter(EntitysModel.id == id).first()
        )

        if not entityOutput:
            return None

        entityOutput.data = date.today()
        entityOutput.sistema = entityInput.sistema
        entityOutput.unidade = entityInput.unidade
        entityOutput.entity_name = entityInput.entity_name
        entityOutput.oldExternalId = entityInput.oldExternalId
        entityOutput.newExternalId = entityInput.newExternalId

        self.session.commit()

        return entityOutput

    # ///////////////////////////////////////////////
    #                   delete
    # ///////////////////////////////////////////////
    def delete(self, id: int) -> EntitysModel:

        entityOutput = (
            self.session.query(EntitysModel).filter(EntitysModel.id == id).first()
        )

        if not entityOutput:
            return False
        self.session.delete(entityOutput)
        self.session.commit()

        return entityOutput

    def find(
        self,
        data: date | None = None,
        sistema: str | None = None,
        unidade: str | None = None,
    ):
        filtros = []

        if data:
            filtros.append(EntitysModel.data == data)

        if sistema:
            filtros.append(EntitysModel.sistema == sistema)

        if unidade:
            filtros.append(EntitysModel.sistema == unidade)

        stmt = select(EntitysModel)

        if filtros:
            stmt = stmt.where(*filtros)

        return self.session.scalars(stmt).all()
