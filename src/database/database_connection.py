from src.interface.databaseInterface.database_interface import DataBaseInterface
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class DatabaseConnection(DataBaseInterface[Session]):
    def __init__(self):
        self.base = Base

    def bootstrap(
        self,
        endatabase_url="sqlite:///src/database/database.db",
    ) -> Session:

        engine = create_engine(endatabase_url)

        session = sessionmaker(bind=engine)

        self.base.metadata.create_all(engine)

        return session
