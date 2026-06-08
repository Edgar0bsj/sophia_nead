from datetime import date

from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.models.entitys_model import EntitysModel


class EntityRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create(self, entitys_model: EntitysModel) -> EntitysModel:
        self.session.add(entitys_model)
        self.session.commit()
        return entitys_model

    def find_all(self) -> list[EntitysModel]:
        return self.session.query(EntitysModel).all()

    def update(self, _id: int, entitys_model: EntitysModel) -> EntitysModel | None:
        newEntity = self.session.query(EntitysModel).filter_by(id=_id).first()

        newEntity.sistema = entitys_model.sistema
        newEntity.unidade = entitys_model.unidade
        newEntity.entity_name = entitys_model.entity_name
        newEntity.oldExternalId = entitys_model.oldExternalId
        newEntity.newExternalId = entitys_model.newExternalId

        self.session.commit()
        return newEntity

    def delete(self, _id: int) -> EntitysModel | None:
        findEntity = self.session.query(EntitysModel).filter_by(id=_id).first()
        self.session.delete(findEntity)
        self.session.commit()
        return findEntity

    def find_by_data(self, data: date) -> list[EntitysModel] | None:
        all_entity = (
            self.session.query(EntitysModel).filter(EntitysModel.data == data).all()
        )

        return all_entity
