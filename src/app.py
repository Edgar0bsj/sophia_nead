from src.database.create_tables import create_tables
from src.controllers.alunoController.aluno_controller import AlunoController
from src.schemas.aluno_schema import AlunoCreate


create_tables()
controller = AlunoController()

controller.criar(AlunoCreate(nome="marcus", cargo="ll"))

