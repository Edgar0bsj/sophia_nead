from sqlalchemy import Boolean, Date, ForeignKey, String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from src.database.base import Base


class CurriculoModel(Base):
    __tablename__ = "curriculo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    externalCourseId: Mapped[str] = mapped_column(
        ForeignKey("cursos.externalId", ondelete="CASCADE")
    )

    name: Mapped[str] = mapped_column(String(150))

    externalId: Mapped[str] = mapped_column(String(100), unique=True)

    workload: Mapped[float] = mapped_column(Float)

    startDate: Mapped[date | None] = mapped_column(Date, nullable=True)

    endDate: Mapped[date | None] = mapped_column(Date, nullable=True)

    isActive: Mapped[bool] = mapped_column(Boolean)

    curso: Mapped["CursosModel"] = relationship(  # type: ignore
        back_populates="curriculos", passive_deletes=True
    )
