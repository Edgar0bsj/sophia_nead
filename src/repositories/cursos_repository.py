from datetime import date

from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.models.cursos_model import CursosModel


class CursosRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create(self, cursos_model: CursosModel) -> CursosModel:
        self.session.add(cursos_model)
        self.session.commit()
        return cursos_model

    def find_all(self) -> list[CursosModel]:
        return self.session.query(CursosModel).all()

    def update(self, _id: int, cursos_model: CursosModel) -> CursosModel | None:
        newCursos = self.session.query(CursosModel).filter_by(id=_id).first()

        newCursos.sistema = cursos_model.sistema
        newCursos.unidade = cursos_model.unidade
        newCursos.name = cursos_model.name
        newCursos.externalId = cursos_model.externalId
        newCursos.isActive = cursos_model.isActive
        newCursos.externalTeachingModalityId = cursos_model.externalTeachingModalityId
        newCursos.externalEducationLevelId = cursos_model.externalEducationLevelId
        newCursos.courseTypeId = cursos_model.courseTypeId

        self.session.commit()
        return newCursos

    def delete(self, _id: int) -> CursosModel | None:
        findCursos = self.session.query(CursosModel).filter_by(id=_id).first()
        self.session.delete(findCursos)
        self.session.commit()
        return findCursos

    def find_by_data(self, data: date) -> list[CursosModel] | None:
        all_cursos = (
            self.session.query(CursosModel).filter(CursosModel.data == data).all()
        )

        return all_cursos
