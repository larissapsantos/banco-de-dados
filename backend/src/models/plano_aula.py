from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import text
from src.database import Base

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