from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy import text
from src.database import Base

class Professor(Base):
    __tablename__ = "professor"

    matricula = Column("matricula", Integer, primary_key=True)
    nome = Column("nome", String(100))
    situacao = Column("situacao", String(50))
    id_escola = Column(Integer, ForeignKey("escola.id"), nullable=False)