from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import text
from src.database import Base

class Escola(Base):
    __tablename__ = "escola"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    bairro = Column("bairro", String)
    uf = Column("uf", String)
    ano_inauguracao = Column("ano_inauguracao", Integer)