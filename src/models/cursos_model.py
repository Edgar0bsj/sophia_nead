from sqlalchemy import Date, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from src.database.base import Base


class CursosModel(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    name: Mapped[str] = mapped_column(String(100))

    externalId: Mapped[str] = mapped_column(String(100), unique=True)

    isActive: Mapped[bool] = mapped_column(Boolean)

    externalTeachingModalityId: Mapped[str] = mapped_column(
        ForeignKey("modalidade.externalId", ondelete="CASCADE")
    )

    externalEducationLevelId: Mapped[str] = mapped_column(
        ForeignKey("niveis_de_ensino.externalId")
    )

    courseTypeId: Mapped[str] = mapped_column(String(100))

    # relacionamentos
    modalidade: Mapped["ModalidadeModel"] = relationship(back_populates="cursos", passive_deletes=True)  # type: ignore
    nivel_de_ensino: Mapped["NiveisDeEnsinoModel"] = relationship(  # type: ignore
        back_populates="cursos", passive_deletes=True
    )
