from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
from sqlalchemy import text
from src.database import Base

class Coordenador(Base):
        __tablename__ = "coordenador"

        matricula = Column("matricula", Integer, primary_key=True)
        nome = Column("nome", String(100))
        situacao = Column("situacao", String(50))
        id_escola = Column(Integer, ForeignKey("escola.id"), nullable=False)