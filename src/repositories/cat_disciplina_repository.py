from datetime import date

from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.models.cat_disciplina_model import CategoriasDaDisciplinaModel


class CategoriasDaDisciplinaRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create(
        self, cat_disciplina: CategoriasDaDisciplinaModel
    ) -> CategoriasDaDisciplinaModel:
        self.session.add(cat_disciplina)
        self.session.commit()
        return cat_disciplina

    def find_all(self) -> list[CategoriasDaDisciplinaModel]:
        return self.session.query(CategoriasDaDisciplinaModel).all()

    def update(
        self, _id: int, cat_disciplina: CategoriasDaDisciplinaModel
    ) -> CategoriasDaDisciplinaModel | None:
        new_cat_disciplina = (
            self.session.query(CategoriasDaDisciplinaModel).filter_by(id=_id).first()
        )

        new_cat_disciplina.sistema = cat_disciplina.sistema
        new_cat_disciplina.unidade = cat_disciplina.unidade
        new_cat_disciplina.name = cat_disciplina.name
        new_cat_disciplina.externalId = cat_disciplina.externalId
        new_cat_disciplina.subjectCategoryTypeId = cat_disciplina.subjectCategoryTypeId
        new_cat_disciplina.isActive = cat_disciplina.isActive

        self.session.commit()
        return new_cat_disciplina

    def delete(self, _id: int) -> CategoriasDaDisciplinaModel | None:
        find_cat_disciplina = (
            self.session.query(CategoriasDaDisciplinaModel).filter_by(id=_id).first()
        )
        self.session.delete(find_cat_disciplina)
        self.session.commit()
        return find_cat_disciplina

    def find_by_data(self, data: date) -> list[CategoriasDaDisciplinaModel] | None:
        all_cat_disciplina = (
            self.session.query(CategoriasDaDisciplinaModel)
            .filter(CategoriasDaDisciplinaModel.data == data)
            .all()
        )

        return all_cat_disciplina
