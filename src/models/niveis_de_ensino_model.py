from sqlalchemy import Date, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from src.database.base import Base


class NiveisDeEnsinoModel(Base):
    __tablename__ = "niveis_de_ensino"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    name: Mapped[str] = mapped_column(String(100))

    externalId: Mapped[str] = mapped_column(String(100), unique=True)

    educationLevelTypeId: Mapped[str] = mapped_column(String(100))

    # Relacionamento
    cursos: Mapped[list["CursosModel"]] = relationship(  # type: ignore
        back_populates="nivel_de_ensino", passive_deletes=True
    )
