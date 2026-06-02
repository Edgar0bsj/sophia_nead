from sqlalchemy import Date, String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.database.database_connection import Base


class PessoasModel(Base):
    __tablename__ = "pessoas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    data: Mapped[date] = mapped_column(Date, default=date.today)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    pessoa_name: Mapped[str] = mapped_column(String(50))

    socialName: Mapped[str] = mapped_column(String(50))

    identityDocument: Mapped[str] = mapped_column(String(20))

    identityDocumentTypeId: Mapped[bool] = mapped_column(String(250))

    passportNumber: Mapped[bool] = mapped_column(String(250))

    externalId: Mapped[bool] = mapped_column(String(250))

    address_zipCode: Mapped[bool] = mapped_column(String(250))

    address_state: Mapped[bool] = mapped_column(String(250))

    address_city: Mapped[bool] = mapped_column(String(250))

    address_address: Mapped[bool] = mapped_column(String(250))

    address_number: Mapped[bool] = mapped_column(String(250))

    address_neighborhood: Mapped[bool] = mapped_column(String(250))

    address_complement: Mapped[bool] = mapped_column(String(250))

    user_email: Mapped[bool] = mapped_column(String(250))

    user_username: Mapped[bool] = mapped_column(String(250))

    user_password: Mapped[bool] = mapped_column(String(250))

    tags: Mapped[bool] = mapped_column(String(250))
