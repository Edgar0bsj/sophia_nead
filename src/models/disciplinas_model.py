from sqlalchemy import Date, String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.database.base import Base


class DisciplinasModel(Base):
    __tablename__ = "disciplinas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    disciplina_name: Mapped[str] = mapped_column(String(200))

    externalId: Mapped[str] = mapped_column(String(50))

    workload: Mapped[int] = mapped_column(Integer)

    isActive: Mapped[bool] = mapped_column(Boolean)

    externalSubjectCategoryId: Mapped[str] = mapped_column(String(50))
