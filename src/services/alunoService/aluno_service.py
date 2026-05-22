from src.repositories.aluno.aluno_repository import AlunoRepository

class AlunoService:

    def __init__(self):
        self.repository = AlunoRepository()

    def criar_aluno(self, nome, cargo):


        return self.repository.criar(
            nome,
            cargo
        )
        
    def buscar_todos(self):
        return self.repository.listar_todos()