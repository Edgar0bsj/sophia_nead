from sqlalchemy import Boolean, Date, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.database.base import Base


class CategoriasDaDisciplinaModel(Base):
    __tablename__ = "categorias_disciplina"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    name: Mapped[str] = mapped_column(String(100))

    externalId: Mapped[str] = mapped_column(String(50), unique=True)

    subjectCategoryTypeId: Mapped[str] = mapped_column(String(20))

    isActive: Mapped[bool] = mapped_column(Boolean)
