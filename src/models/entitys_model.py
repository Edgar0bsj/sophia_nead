from sqlalchemy import Date, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date


from src.database.base import Base

class EntitysModel(Base):
    __tablename__ = "entitys_model"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    data: Mapped[date] = mapped_column(Date, default=date.today)
    
    sistema: Mapped[date] = mapped_column(String(100))
    
    unidade: Mapped[date] = mapped_column(String(100))
    
    entity_name: Mapped[str] = mapped_column(String(100))
    
    oldExternalId: Mapped[str] = mapped_column(String(100))
    
    newExternalId: Mapped[str] = mapped_column(String(100))