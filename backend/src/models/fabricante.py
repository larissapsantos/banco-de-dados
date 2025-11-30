from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import text
from src.database import Base

class Fabricante(Base):
    __tablename__ = "fabricante"

    cnpj = Column("cnpj", Integer, primary_key=True)
    nome = Column("nome", String(100))
    bairro = Column("bairro", String(100))
    uf = Column("uf", String(2))
    telefone = Column("telefone", String(11))