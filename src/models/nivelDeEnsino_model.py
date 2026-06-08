from sqlalchemy import Date, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from database.base import Base


class NivelDeEnsinoModel(Base):
    __tablename__ = "nivel_de_ensino"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    NivelDeEnsino_name: Mapped[str] = mapped_column(String(100))

    externalId: Mapped[str] = mapped_column(String(100))

    educationLevelTypeId: Mapped[str] = mapped_column(String(100))
