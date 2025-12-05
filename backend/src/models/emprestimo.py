from sqlalchemy import DateTime, create_engine, Column, Integer, ForeignKey
from sqlalchemy import text
from src.database import Base
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Emprestimo(Base):
        __tablename__ = "emprestimo"

        id = Column("id", Integer, primary_key=True, autoincrement=True)
        data_hora = Column("data_hora", DateTime, nullable=False)
        id_escola = Column(Integer, ForeignKey("escola.id"), nullable=False)
        id_equipamento = Column(Integer, ForeignKey("equipamento.id"), nullable=False)
        id_plano_aula = Column(Integer,ForeignKey("plano_aula.id"), nullable=False)

        def __init__(self, id_escola, id_equipamento, id_plano_aula):
            self.id_escola = id_escola 
            self.id_equipamento = id_equipamento 
            self.id_plano_aula = id_plano_aula

class EmprestimoSchema(BaseModel):
    data_hora: datetime = Field(default_factory=datetime.now)
    id_escola: int
    id_equipamento: int
    id_plano_aula: int

class AtualizarEmprestimoSchema(BaseModel):
    data_hora: Optional[datetime] = Field(default_factory=datetime.now)
    id_escola: Optional[int] = None
    id_equipamento: Optional[int] = None
    id_plano_aula: Optional[int] = None