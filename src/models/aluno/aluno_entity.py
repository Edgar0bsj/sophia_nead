from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(
        String(100)
    )

    cargo: Mapped[str] = mapped_column(
        String(100)
    )