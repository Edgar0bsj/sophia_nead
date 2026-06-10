from sqlalchemy import JSON, Date, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.database.base import Base


class PessoasModel(Base):
    """
    `feat futura:` campos user_password | user_email
    pode vim vazio, nesse caso deve apontar um aviso
    """

    __tablename__ = "pessoas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    name: Mapped[str] = mapped_column(String(100))

    socialName: Mapped[str] = mapped_column(String(100), nullable=True)

    identityDocument: Mapped[str] = mapped_column(String(100))

    identityDocumentTypeId: Mapped[str] = mapped_column(String(100))

    passportNumber: Mapped[str] = mapped_column(String(100), nullable=True)

    externalId: Mapped[str] = mapped_column(String(100), unique=True)

    address_zipCode: Mapped[str] = mapped_column(String(100), nullable=True)

    address_state: Mapped[str] = mapped_column(String(100), nullable=True)

    address_city: Mapped[str] = mapped_column(String(100), nullable=True)

    address_address: Mapped[str] = mapped_column(String(100), nullable=True)

    address_number: Mapped[str] = mapped_column(String(100), nullable=True)

    address_neighborhood: Mapped[str] = mapped_column(String(100), nullable=True)

    address_complement: Mapped[str] = mapped_column(String(100), nullable=True)

    user_email: Mapped[str] = mapped_column(String(100))

    user_username: Mapped[str] = mapped_column(String(100), unique=True)

    user_password: Mapped[str] = mapped_column(String(100))

    tags: Mapped[list[str]] = mapped_column(JSON, nullable=True)
    """
    **Inserindo dados nessa coluna**
    PessoasModel.tags = ["UNIG", "2 Entrada"]
    """
