from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy import text
from src.database import Base
from pydantic import BaseModel

class Solicitacao(Base):
    __tablename__ = "solicitacao"

    id_administrador = Column("id_servidor", ForeignKey("administrador.matricula"), primary_key=True)
    id_emprestimo = Column("id_emprestimo", ForeignKey("emprestimo.id"), primary_key=True)
    id_coordenador = Column("id_coordenador", ForeignKey("coordenador.matricula"), primary_key=True)
    status = Column("status", String(50))

    def __init__(self, id_administrador, id_emprestimo, id_coordenador, status= "EM ANÁLISE"):
        self.id_administrador = id_administrador
        self.id_emprestimo = id_emprestimo
        self.id_coordenador = id_coordenador
        self.status = status

class SolicitacaoSchema(BaseModel):
    id_servidor: int
    id_emprestimo: int
    id_coordenador: int
    status: str

class AtualizarSolicitacaoSchema(BaseModel):
    status: str

class ConsolidacaoSolicitacaoSchema(BaseModel):
    solicitacoes_ids: list[dict]