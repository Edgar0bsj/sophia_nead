from sqlalchemy import Date, String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.database.database_connection import Base


class CategoriasDaDiciplinaModel(Base):
    __tablename__ = "categoria_disciplina"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    categoria_da_diciplina_name: Mapped[str] = mapped_column(String(50))

    externalId: Mapped[str] = mapped_column(String(50))

    subjectCategoryTypeId: Mapped[str] = mapped_column(String(20))

    isActive: Mapped[bool] = mapped_column(Boolean)
