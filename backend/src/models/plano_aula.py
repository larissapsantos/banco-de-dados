from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import text
from sqlalchemy_utils.types import ChoiceType
from src.database import Base

class PlanoAula(Base):
    __tablename__ = "plano_aula"
    STATUS_SOLICITACAO =(
        ("EM ANÁLISE", "EM ANÁLISE"), 
        ("CANCELADA", "CANCELADA"),
        ("RECUSADA", "RECUSADA"),
        ("APROVADA", "APROVADA")
        )

    id = Column("id", primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    descricao = Column("descricao", String)
    status = Column("status", ChoiceType(choices=STATUS_SOLICITACAO), default="EM ANÁLISE")
    id_professor = Column("id_professor", Integer)

    def __init__(self, titulo, descricao, status, id_professor):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.id_professor = id_professor