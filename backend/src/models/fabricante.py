from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import text
from src.database import Base

class Fabricante(Base):
    __tablename__ = "fabricante"

    cnpj = Column("cnpj", Integer, primary_key=True)
    nome = Column("nome", String)
    bairro = Column("bairro", String)
    uf = Column("uf", String)
    telefone = Column("telefone", String)