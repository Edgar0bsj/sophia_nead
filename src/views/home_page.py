import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from typing import Optional
from src.ui.assistente_de_importacoes import Ui_MainWindow as AssImportacoes

class HomePage(QtWidgets.QMainWindow):
    
    def __init__(self)-> None:
        super().__init__()
        
        self.ui = AssImportacoes()
        
        self.ui.setupUi(self)
        
        self.resize(800,580)
        self.setMinimumSize(800,580)
        self.setMaximumSize(800,580)
        
        self.setWindowTitle("Assistente de importacoes")
        
        # EVENTOS
        # BTNS
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnSelecionarArquivo.clicked.connect(self.selecionar_arquivo)
        self.ui.btnAnalisar.clicked.connect(self._analisar_evento)
        self.ui.btnSalvar.clicked.connect(self._salvar_evento)
        
        # Combo box
        self.ui.cbAssistenteImportacoes.currentTextChanged.connect(self.cbGrupo_opcoes)
        
        self._dataPath:Optional[str] = None
        
        
    def _selecionar_arquivo_evento(self):
        print("BUTTON SELEÇÃO FUNCIONANDO")
        
    def _analisar_evento(self):
        print("BTN ANALISAR FUNCIONANDO")
        self.ui.btnSalvar.setEnabled(True)
        
    def _salvar_evento(self):
        print("BTN SALVAR FUNCIONANDO")
        
    
    def cbGrupo_opcoes(self, texto):
        self.ui.cbGrupo.clear()

        dados = {
            "Grupos inicial": ["Conjunto de grupos", "Grupo", "Pessoas dos grupos"],
            "Plataforma A": [
                "Todos",
                "Alteração de código externo",
                "Modalidades de ensino",
                "Níveis de ensino",
                "Cursos",
                "Currículos",
                "Categorias da disciplina",
                "Pessoas",
                "Disciplinas",
                "Acessibilidades das pessoas",
                "Disciplinas dos currículos",
                "Períodos",
                "Contatos das pessoas",
                "Turnos",
                "Turmas",
                "Campus",
                "Turmas/Disciplinas",
                "Polos",
                "Papéis de turmas/disciplinas",
                "Pessoas das turmas/disciplinas",
                "Coordenadores",
                "Coordenadores dos cursos",
                "Estudantes",
                "Situações da matrícula",
                "Situações da enturmação",
                "Grupos de matrícula",
                "Tipos de matrícula",
                "Matrículas",
                "Matriculas no período",
                "Enturmações"
                ],
            "Plataforma A (Simplificado)": ["Pessoas", "Turmas/Disciplinas (Simplificado)", "Pessoas das turmas/disciplinas"],
            "Plataforma A (Simplificado 2.0)": [
                "Modalidades de ensino",
                "Níveis de ensino",
                "Cursos",
                "Pessoas",
                "Turmas/Disciplinas (Simplificado)",
                "Pessoas das turmas/disciplinas",
                "Coordenadores",
                "Coordenadores dos cursos",
                ],
        }
        
        self.ui.cbGrupo.addItems(
            dados.get(texto,[])
        )
        
    def selecionar_arquivo(self):
        caminho_arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar Arquivo Excel",
            "",
            "Arquivos Excel (*.xlsx)"
        )

        if caminho_arquivo:

            self.ui.inputArquivo.setText(caminho_arquivo)

            # log
            self.set_log(f"Arquivo selecionado: {caminho_arquivo}")

            self._dataPath = caminho_arquivo
            print(self._dataPath)
        
    def set_log(self, text):
        self.ui.logArea.appendPlainText(text)
