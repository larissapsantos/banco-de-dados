from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import text
from src.database import Base

class Escola(Base):
    __tablename__ = "escola"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(100))
    bairro = Column("bairro", String(100))
    uf = Column("uf", String(2))
    ano_inauguracao = Column("ano_inauguracao", Integer)