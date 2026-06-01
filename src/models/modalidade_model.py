from sqlalchemy import Date, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.database.database_connection import Base


class ModalidadeModel(Base):
    __tablename__ = "modalidade"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    data: Mapped[date] = mapped_column(Date, default=date.today)
    
    sistema: Mapped[str] = mapped_column(String(100))
    
    unidade: Mapped[str] = mapped_column(String(100))
    
    modalidade_nome: Mapped[str] = mapped_column(String(100))
    
    externalId: Mapped[str] = mapped_column(String(100))
    
    teachingModalityTypeId: Mapped[str] = mapped_column(String(100))