from src.models.aluno.aluno_entity import Aluno
from src.database.connection import SessionLocal

class AlunoRepository:

    def __init__(self):
        self.session = SessionLocal()

    def criar(self, nome, cargo):

        aluno = Aluno(
            nome=nome,
            cargo=cargo
        )

        self.session.add(aluno)
        self.session.commit()

        return aluno

    def listar_todos(self):
        return self.session.query(Aluno).all()