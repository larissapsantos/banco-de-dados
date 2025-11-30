from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy import text
from sqlalchemy_utils.types import ChoiceType
from src.database import Base

class Solicitacao(Base):
    __tablename__ = "solicitacao"
    STATUS_SOLICITACAO = (
        ("EM ANÁLISE", "EM ANÁLISE"), 
        ("CANCELADA", "CANCELADA"),
        ("RECUSADA", "RECUSADA"),
        ("APROVADA", "APROVADA")
        )

    id_administrador = Column("id_servidor", ForeignKey("servidor_adm.matricula"), primary_key=True)
    id_emprestimo = Column("id_emprestimo", ForeignKey("emprestimo.id"), primary_key=True)
    id_coordenador = Column("id_coordenador", ForeignKey("coordenador.matricula"), primary_key=True)
    status = Column("status", ChoiceType(choices=STATUS_SOLICITACAO), default="EM ANÁLISE")

    def __init__(self, id_administrador, id_emprestimo, id_coordenador, status= "EM ANÁLISE"):
        self.id_administrador = id_administrador
        self.id_emprestimo = id_emprestimo
        self.id_coordenador = id_coordenador
        self.status = status