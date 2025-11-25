from .equipamento import Equipamento

from .kit_robotica import KitRobotica
from .material import Material
from .impressora_3d import Impressora3D

from .escola import Escola
from .professor import Professor
from .coordenador import Coordenador
from .administrador import Administrador
from .solicitacao import Solicitacao
from .plano_aula import PlanoAula
from .emprestimo import Emprestimo

__all__ = [
    "Equipamento",
    "KitRobotica",
    "Material",
    "Impressora3D",
    "Escola",
    "Professor",
    "Coordenador",
    "Administrador",
    "Solicitacao",
    "PlanoAula",
    "Emprestimo"
]