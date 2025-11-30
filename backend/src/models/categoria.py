from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import text
from src.database import Base

class Categoria(Base):
    __tablename__ = "categoria"

    id = Column("id", Integer, primary_key=True)
    descricao = Column("descricao", String(300))
    nome = Column("nome", String(100))