from dataclasses import dataclass
from enum import Enum


class EntityEnum(Enum):
    ACESSIBILIDADES = "accessibility"
    CAMPUS = "campus"
    TURMAS = "class"
    CURSOS = "course"
    CURRICULOS = "curriculum"
    POLOS = "educational-hub"
    NIVEIS_DE_ENSINO = "education-level"
    MATRICULAS = "enrollment"
    SITUACOES_DA_ENTURMACAO = "enrollment-class-subject-status"
    GRUPOS_DE_MATRICULA = "enrollment-group"
    MATRICULAS_NO_PERIODO = "enrollment-period"
    SITUACOES_DA_MATRICULA = "enrollment-status"
    TIPOS_DE_MATRICULA = "enrollment-type"
    INTAKES = "intake"
    PERIODOS = "period"
    PESSOAS = "person"
    TURNOS = "shift"
    DISCIPLINAS = "subject"
    CATEGORIAS_DA_DISCIPLINA = "subject-category"
    MODALIDADES_DE_ENSINO = "teaching-modality"
    TURMAS_DISCIPLINAS = "class-subject"
    PAPEIS_DE_TURMAS_DISCIPLINAS = "class-subject-role"


@dataclass(frozen=True)
class EntityInputDTO:
    sistema: str
    unidade: str

    entity: EntityEnum
    oldExternalId: str
    newExternalId: str
