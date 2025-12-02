from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import text
from src.database import Base
from pydantic import BaseModel
from typing import Optional

class PlanoAula(Base):
    __tablename__ = "plano_aula"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String(100), nullable=False)
    descricao = Column("descricao", String(500))
    status = Column("status", String(50))
    id_professor = Column(Integer, ForeignKey("professor.matricula"), nullable=False)
    id_coordenador = Column(Integer, ForeignKey("coordenador.matricula"), nullable=False)

    def __init__(self, titulo, descricao, status, id_professor, id_coordenador):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.id_professor = id_professor
        self.id_coordenador = id_coordenador
    
class PlanoAulaSchema(BaseModel):
    titulo: str
    descricao: str
    status: str
    id_professor: int
    id_coordenador: int

class ConsolidacaoPlanoSchema(BaseModel):
    id_coordenador: int
    planos_ids: list[int]

class AprovarPlanoSchema(BaseModel):
    status: str

class AtualizarPlanoAulaSchema(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[str] = None
    id_professor: Optional[int] = None
    id_coordenador: Optional[int] = None