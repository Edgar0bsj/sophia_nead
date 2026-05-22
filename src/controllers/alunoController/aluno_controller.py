from src.services.alunoService.aluno_service import AlunoService
from src.schemas.aluno_schema import AlunoCreate


class AlunoController:

    def __init__(self):
        self.service = AlunoService()

    def criar(self, aluno:AlunoCreate):
        return self.service.criar_aluno(**aluno.__dict__)
    
    def listar(self):
        return self.listar()