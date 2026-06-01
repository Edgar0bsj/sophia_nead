from sqlalchemy import Date, String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.database.database_connection import Base


class CursosModel(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    cursos_name: Mapped[str] = mapped_column(String(100))

    externalId: Mapped[str] = mapped_column(String(100))

    isActive: Mapped[bool] = mapped_column(Boolean)

    externalTeachingModalityId: Mapped[str] = mapped_column(String(100))

    externalEducationLevelId: Mapped[str] = mapped_column(String(100))

    courseTypeId: Mapped[str] = mapped_column(String(100))
