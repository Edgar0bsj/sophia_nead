from sqlalchemy import Date, String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.database.database_connection import Base


class CurriculoModel(Base):
    __tablename__ = "curriculos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    externalCourseId: Mapped[str] = mapped_column(String(50))

    curriculo_name: Mapped[str] = mapped_column(String(150))

    externalId: Mapped[str] = mapped_column(String(50))

    workload: Mapped[int] = mapped_column(Integer)

    startDate: Mapped[date] = mapped_column(Date)

    endDate: Mapped[date] = mapped_column(Date)

    isActive: Mapped[bool] = mapped_column(Boolean)
