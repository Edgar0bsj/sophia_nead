from src.database.base import Base
from src.database.connection import engine

from src.models.aluno.aluno_entity import Aluno


def create_tables():
    Base.metadata.create_all(engine)
    
    return 